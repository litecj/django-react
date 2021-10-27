import csv
from datetime import datetime

import pandas as pd
from bs4 import BeautifulSoup
from django.db import models
from tweepy.streaming import Stream, StreamListener

# Create your models here.
from admin.common.models import ValueObject
from selenium import webdriver

from nltk import FreqDist # 한국어 빈도수 체크
from wordcloud import WordCloud
import matplotlib.pyplot as plt


from konlpy.tag import Okt  # 한국어 처리 프로세서
from nltk.tokenize import word_tokenize  # 한국어 처리 프로세서
import nltk
import re


from wordcloud import WordCloud
from matplotlib import pyplot
from collections import Counter
from konlpy.tag import Okt
import os
import requests

class NewsCrawling(object):
    # 멤버변수(1) - 브라우저 버전 정보 문자열
    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
    # 멤버변수(2) - 접속에 사용될 세션객체 (생성자에서 사용된다.)
    session = None
    # -----------------------------------------------------
    # 생성자 - 접속 세션을 생성한다.
    # -----------------------------------------------------
    def __init__(self, referer=''):
        vo = ValueObject()
        vo.context = 'admin/crawling/data/'
        ses_info = {'referer': referer, 'User-agent': self.user_agent}
        # 세션객체 생성
        self.session = requests.Session()
        # 세션에 접속 정보 설정
        self.session.headers.update(ses_info)

        #-----------------------------------------------------
        # HTML 페이지에 접속하여 페이지의 모든 소스코드를 가져온다.
        #-----------------------------------------------------
    def get(self, url, encoding='utf-8'):
        # 생성자에서 만든 세션 객체를 사용하여 URL에 접근
        r = self.session.get(url)

        # 에러가 발생했다면 None을 리턴하고 처리 중단
        if r.status_code != 200:
            return None

        # 인코딩 설정
        r.encoding = encoding

        # 결과 문자열의 앞,뒤 공백을 제거한 상태로 리턴
        return r.text.strip()

    #-----------------------------------------------------
    # HTML 페이지에 접속하여 특정 셀렉터에 대하여 파싱한 결과를 List로 반환한다.
    #-----------------------------------------------------
    def select(self, url, selector='html', encoding='utf-8'):
        # 웹 페이지 접속 함수를 호출하여 소스코드 리턴받기
        source = self.get(url, encoding)

        # 리턴값이 없다면 처리 중단
        if not source:
            return None

        # 웹 페이지의 소스코드 HTML 분석 객체로 생성
        soup = BeautifulSoup(source, 'html.parser')

        # CSS 선택자를 활용하여 가져오기를 원하는 부분 지정
        # -> list로 리턴
        return soup.select(selector)

    #-----------------------------------------------------
    # 크롤링한 결과 원본(item)에서 tag와 selector가 일치하는 항목을 삭제
    #-----------------------------------------------------
    def remove(self, item, tag, selector=None):
        for target in item.find_all(tag, selector):
            target.extract()

    #-----------------------------------------------------
    # 특정 URL의 파일을 다운로드 한다.
    #-----------------------------------------------------
    def download(self, url, filename=""):
        # 접속 객체를 사용하여 파라미터로 전달된 URL 다운로드 받기
        r = self.session.get(url, stream=True)


    # 에러여부 검사 - 에러가 발생했다면 None을 리턴하며 처리 종료
        if r.status_code != 200:
            return None
        # 이미지의 byte 데이터를 추출
        img = r.raw.read()
        # 추출한 데이터를 저장
        with open(filename, 'wb') as f:
            f.write(img)
        # 저장된 파일 이름만 리턴
        return filename

# 크롤링 클래스에 대한 객체를 생성
# -> 이 파일을 모듈로서 참조하는 다른 파일이 사용할 수 있다.
# crawler = Crawler()
    '''
        !pip install git+https://git@github.com/kavgan/word_cloud.git
        
        
        !apt-get update 
        !apt-get install g++ openjdk-8-jdk python-dev python3-dev 
        !pip3 install JPype1-py3 
        !pip3 install konlpy 
        !JAVA_HOME="C:\Program Files\Java\jdk1.8.0_241"
        
        
        import matplotlib as mpl
        import matplotlib.pyplot as plt
        %config InlineBackend.figure_format = 'retina'
        !apt -qq -y install fonts-nanum
        import matplotlib.font_manager as fm
        fontpath = 'C:/Windows/Fonts/NanumGothic-Regular.ttf'
        font = fm.FontProperties(fname=fontpath, size=9)
        plt.rc('font', family='NanumBarunGothic') 
        mpl.font_manager._rebuild()
    
        from google.colab import auth
        auth.authenticate_user()
        from google.colab import drive
        drive.mount('/content/gdrive')
    '''



    def process(self):
        context = self.vo.context
        # ------------------------------------------------------------
        # 1) 접속조건 설정하기
        # ------------------------------------------------------------
        URL = "https://news.naver.com/"
        url_list = []  # 뉴스기사의 본문 URL을 저장할 리스트
        # ------------------------------------------------------------
        # 2) 수집할 뉴스기사의 URL 조사하기
        # ------------------------------------------------------------
        # 가져온 URL에서 링크에 대한 셀렉터를 크롤링 -> 반환결과는 List형태
        # -> 여러 형식의 셀렉터를 동시에 처리해야 할 경우 콤마(,)로 구분하여 지정한다.
        link_list = self.select(URL, encoding="euc-kr",
                                selector=".newsnow_tx_inner > a, .newsnow_imgarea > a, .mtype_img > dt > a, .mlist2 > li > a")
        # 가져온 결과 확인하기
        for item in link_list:
            print(item)
        print("-" * 30)
        # 리스트의 원소들에 대한 반복 처리
        for item in link_list:
            print(type(item.attrs))
        # 각 원소(링크)에 속성들(attrs) 중에
        # href 속성이 있다면 그 속성값을 별도로 준비한 리스트에 추가
        if "href" in item.attrs:
            # href속성은 링크를 클릭했을 때의 URL을 의미한다.
            # URL에 뉴스 상세 페이지의 파일명인 "read.nhn"이 포함되어 있다면
            # 해당 주소를 url_list에 추가한다.
            if "read.nhn" in item['href']:
                url_list.append(item['href'])
        # 집계된 리스트의 주소들 확인하기
        for v in url_list:
            print(v)
        # ------------------------------------------------------------
        # 3) 뉴스기사에 접속하여 본문 크롤링 하기
        # ------------------------------------------------------------
        print("=" * 50)
        print("뉴스기사 크롤링 시작 >> 총 %d개의 기사를 수집합니다." % len(url_list))
        print("=" * 50)
        # 기사의 본문을 누적해서 저장할 문자열 변수
        news_content = ''
        # URL 목록만큼 반복
        for i, url in enumerate(url_list):
            print("%d번째 뉴스기사 수집중... >> %s" % (i + 1, url))
        # URL에 접근하여 뉴스 컨텐츠를 가져온다.
        news_html = self.select(url, selector='#articleBodyContents', encoding='euc-kr')
        if not news_html:  # 가져온 내용이 없다면?
            print("%d번째 뉴스기사 크롤링 실패" % (i + 1))
        else:  # 가져온 내용이 있다면?
            print("%d번째 뉴스기사 크롤링 성공" % (i + 1))
        # 수집결과에서 불필요한 HTML 태그 제거
        for item in news_html:
            self.remove(item, 'script')
        self.remove(item, 'a')
        self.remove(item, 'br')
        self.remove(item, 'span', {'class': 'end_photo_org'})
        # 공백을 제거한 텍스트만 미리 준비한 변수에 누적
        news_content += item.text.strip()

        # ------------------------------------------------------------
        # 4) 수집결과를 기반으로 형태소 분석
        # ------------------------------------------------------------
        # 형태소 분석 객체를 통해 수집된 뉴스 본문에서 명사만 추출
        nlp = Okt()
        nouns = nlp.nouns(news_content)
        # 명사들에 대한 빈도수 검사
        count = Counter(nouns)
        # 가장 많이 사용된 단어 100개 추출
        most = count.most_common(100)
        # 추출 결과를 워드 클라우드에서 요구하는 형식으로 재구성
        # --> {"단어": 빈도수, "단어": 빈도수 ...}
        tags = {}
        for n, c in most:
            if len(n) > 1:
                tags[n] = c
        # ------------------------------------------------------------
        # 5) 수집결과를 활용하여 워드클라우드 생성
        # ------------------------------------------------------------
        # 워드 클라우드 객체 만들기
        wc = WordCloud(font_path=context + "NanumGothic-Regular.ttf", max_font_size=200,
                       width=1200, height=800, scale=2.0, background_color='#ffffff')
        # 미리 준비한 딕셔너리를 통해 생성
        gen = wc.generate_from_frequencies(tags)
        # 워드 클라우드 이미지 저장
        plt.figure()
        plt.imshow(gen, interpolation='bilinear')
        plt.axis("off")
        wc.to_file(context + "news_1.png")
        plt.close()





class Crawling(object):
    def __init__(self):
        pass

    def Process(self):
        vo = ValueObject()
        vo.context = 'admin/crawling/data/'
        # self.naver_movie()
        # self.tweet_trump()
        self.samsung_report(vo)

    def samsung_report(self, vo):
        okt = Okt()
        okt.pos("삼성전자 글로벌센터 전자사업부", stem=True)
        filename = f'{vo.context}kr-Report_2018.txt'
        with open(filename, 'r', encoding='utf-8') as f:
            full_texts = f.read()
        line_removed_texts = full_texts.replace('\n', ' ')
        # print(f':::::::: {datetime.now()} ::::::::\n {line_removed_texts}')
        tokenizer = re.compile(r'[^ ㄱ-힣]+')
        tokenized_texts = tokenizer.sub('', line_removed_texts)
        # print(f':::::::: tokenized_texts ::::::::\n {tokenized_texts}')
        '''
            :::::::: tokenized_texts ::::::::
             삼성전자 지속가능경영보고서              보고서 개요 삼성전자는 경제사회환경적 가치창출의
            통합적인 성과를 다양한 이해관계자에게 투명하게 소통하고자 매년 지속가능경영보고서를 발간하
            고 있으며 년 열한
        '''
        tokens = word_tokenize(tokenized_texts)
        # print(f':::::::: tokens ::::::::\n {tokens}')
        '''
            :::::::: tokens ::::::::
             ['삼성전자', '지속가능경영보고서', '보고서', '개요', '삼성전자는', '경제사회환경적', '가치
            창출의', '통합적인', '성과를', '다양한', '이해관계자에게', '투명하게', '소통하고자', '매년',
        '''
        noun_tokens = []
        for token in tokens:
            token_pos = okt.pos(token)
            noun_token = [txt_tag[0] for txt_tag in token_pos if txt_tag[1] == 'Noun']
            if len(''.join(noun_token)) > 1:
                noun_tokens.append("".join(noun_token))
        # print(f':::::::: noun_tokens ::::::::\n {noun_tokens[:10]}')
        '''
            :::::::: noun_tokens ::::::::
             ['삼성전자', '가능보고서', '보고서', '개요', '전자', '사회환경', '가치창', '통합', '성과',
             '이해관계자']
        '''
        noun_tokens_join = " ".join(noun_tokens)
        # print(f':::::::: noun_tokens_join ::::::::\n {noun_tokens_join}')
        '''
            :::::::: noun_tokens_join ::::::::
             삼성전자 가능보고서 보고서 개요 전자 사회환경 가치창 통합 성과 이해관계자 소통 매년 가능보
            고서 발간 열한 가능보고서 발간 보고기간 보고서 사회환경 성과 활동 일부 정성 성과 대해 자료
            포함 정량
        '''
        tokens = word_tokenize(noun_tokens_join)
        # print(f':::::::: tokens ::::::::\n {tokens}')
        '''
            :::::::: tokens ::::::::
             ['삼성전자', '가능보고서', '보고서', '개요', '전자', '사회환경', '가치창', '통합', '성과', '이해관계자', '소통', '매년', 
             '가능보고서', '발간', '열한', '가능보고서', '발간', '보고기간', '보고서', '사회환경', '성과', '활동', '일부', '정성', 
             '성과', '대해', '자료', '포함', '정량', '연도별', '추이', '분석', '최근', '개년', '수치', '제공', '보고범위', '보고범위', 
             '국내', '해외', '사업', '공급망', '포함', '재무성', '연결기준', '작성', '사업', '환경', '정량', '국내외', '생산'
        '''
        stopfile = f'{vo.context}stopwords.txt'
        with open(stopfile, 'r', encoding='utf-8') as f:
            stopwords = f.read()
        stopwords = stopwords.split(' ')
        stopwords.extend(['각주', '용량', '가능보고서', '고려', '전세계', '릴루미노', '가치창'])
        texts_without_stopwords = [text for text in tokens if text not in stopwords]
        # print(f':::::::: {datetime.now()} ::::::::\n {texts_without_stopwords[:10]}')
        '''
            :::::::: 2021-10-18 15:16:04.681365 ::::::::
            ['사회환경', '열한', '사회환경', '연도별', '추이', '개년', '뉴스룸', '가능사무국', '수원시', '영통구']
        '''
        freq_texts = pd.Series(dict(FreqDist(texts_without_stopwords))).sort_values(ascending=False)
        # print(f':::::::: {datetime.now()} ::::::::\n {freq_texts[:30]}')
        wcloud = WordCloud(f'{vo.context}D2Coding.ttf', relative_scaling=0.2, background_color='white').generate(' '.join(texts_without_stopwords))
        plt.figure(figsize=(12, 12))
        plt.imshow(wcloud, interpolation='bilinear')
        plt.axis('off')
        plt.savefig(f'{vo.context}new_data/wcloud(1).png')


        # okt = Okt()
        # okt.pos('삼성전자 글로벌센터 전자사업부', stem=True)
        # with open(f'{vo.context}kr-Report_2018.txt', 'r', encoding='UTF-8') as f:
        #     texts = f.read()
        # # print(texts)
        # # 워드 프레스를 만들기 위해 쓸모 없는 데이터는 버리고 명사로 한줄 출력 하기 위한 작업
        # temp = texts.replace('\n', ' ')
        # tokenizer = re.compile(r'[^ ㄱ-힣]+')  # f - formatting, r - 정규 표현식으로 []한글자 []+ 여러글자, ^ ㄱ-힣 한글 ㄱ- 끝까지 전부
        # temp = tokenizer.sub('', temp)  # tokenizer 처리 이후 남은 것들은 다 temp 로 처리해라
        # tokens = word_tokenize(temp)
        # noun_token = []
        # for i in tokens:
        #     tokens_pos = okt.pos(i)
        #     temp = [txt_tag[0] for txt_tag in tokens_pos if txt_tag[1] == 'Noun']
        #     if len(''.join(temp)) > 1:
        #         noun_token.append(''.join(temp))
        # texts = ' '.join(noun_token)
        # # print(texts)
        #
        # with open(f'{vo.context}stopwords.txt', 'r', encoding='UTF-8') as f:
        #     stopwords = f.read()
        # stopwords = stopwords.split(' ')
        # # print(f'{datetime.now()}:::::::::\n {stopwords}')
        # texts = [text for text in tokens if text not in stopwords]
        # freqtxt = pd.Series(dict(FreqDist(texts))).sort_values(ascending=False)  # 자주 나온 단어는 가중치를 준다
        # print(f':::::::::\n {freqtxt[:30]}')



    def naver_movie(self):
        vo = ValueObject()
        vo.context = 'admin/crawling/data/'
        vo.url = 'https://movie.naver.com/movie/sdb/rank/rmovie.nhn'
        driver = webdriver.Chrome(f'{vo.context}/chromedriver')
        driver.get(vo.url)
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_div = soup.find_all('div', {'class': 'tit3'})
        arr = [div.a.string for div in all_div]
        for i in arr:
            print(i)
        df = dict(zip([i for i in range(1, 101)], arr))
        # dt = {i + 1: val for i, val in enumerate(arr)}
        print(df)
        pd1 = pd.DataFrame.from_dict(df, orient='index', columns=[ '영화명'])
        print(pd1)
        with open(vo.context+'new_data/with_save.csv', 'w', encoding='UTF-8') as f:
            w = csv.writer(f)
            w.writerow(df.keys())
            w.writerow(df.values())
        # driver.close()




    def tweet_trump(self, dt=None):
        options = webdriver.ChromeOptions()
        options.add_experimental_option("excludeSwitches", ["enable-logging"])
        driver = webdriver.Chrome('admin/crawling/data/chromedriver', options=options)

        start_date = dt.date(year=2018, month=12, day=1)
        until_date = dt.date(year=2018, month=12, day=2)  # 시작날짜 +1
        end_date = dt.date(year=2018, month=12, day=2)
        query = 'Obama'
        total_tweets = []
        url = f'https://twitter.com/search?q={query}%20' \
              f'since%3A{str(start_date)}%20until%3A{str(until_date)}&amp;amp;amp;amp;amp;amp;lang=eg'
        while not end_date == start_date:
            driver.get(url)
            soup = BeautifulSoup(driver.page_source, 'html.parser')
            last_height = driver.execute_script("return document.body.scrollHeight")
            while True:
                daily_freq = {'Date': start_date}
                word_freq = 0
                tweets = soup.find_all('p', {'class': 'TweetWextSize'})
                driver.execute_script('window.scrollTo(0, document.body.scrollHeight);')
                new_height = driver.execute_script('return document.body.scrollHeight')
                if new_height != last_height:
                    soup = BeautifulSoup(driver.page_source, 'html.parser')
                    tweets = soup.find_all('span', {'class', 'css-901oao css-16my406 r-poiln3 r-bcqeeo r-qvutc0'})
                    print('------ 1 ----')
                    print(tweets)
                    word_freq = len(tweets)
                else:
                    daily_freq['Frequency'] = word_freq
                    word_freq = 0
                    start_date = until_date
                    until_date += dt.timedelta(days=1)
                    daily_freq = {}
                    total_tweets.append(tweets)
                    print('------- 2 ---')
                    all_div = soup.find_all('div', {'class', 'css-901oao'})
                    arr = [span.string for span in all_div]
                    for i in arr:
                        print(i)
                    break
                last_height = new_height
        '''
        trump_df = pd.DataFrame(columns=['id', 'message'])
        number = 1
        for i in range(len(total_tweets)):
            for j in range(len(total_tweets[i])):
                trump_df = trump_df.append({'id': number, 'message': (total_tweets[i][j]).text},
                                           ignore_index=True)
                number = number + 1
        print(trump_df.head())
        '''