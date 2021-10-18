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

class Crawling(object):
    def __init__(self):
        pass

    def process(self):
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