from collections import defaultdict

import tensorflow as tf
from tensorflow import keras
import numpy as np
import matplotlib.pyplot as plt
from selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup
import pandas as pd
import csv
from admin.common.models import ValueObject

# Create your models here.
from admin.common.models import ValueObject


class Imdb(object):

    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/nlp/data/'

    def decode_review(self, text, reverse_word_index):
        return ''.join([reverse_word_index.get(i, '?') for i in text])


    # def imdb_process(self):
    #     imdb = keras.datasets.imdb
    #     (train_X, train_Y), (test_X, test_Y) = imdb.load_data(num_words=100000)
    #     word_index = imdb.get_word_index()
    #     word_index = {k: (v+3) for k, v in word_index.items()}
    #     word_index["<PAD>"] = 0
    #     word_index["<START>"] = 1
    #     word_index["<UNK>"] = 2  #UNKNOWN
    #     word_index["<UNUSED>"] = 3
    #     reverse_word_index = dict([(v, k) for (k, v) in word_index.items()])
    #     temp = self.decode_review(train_X[0], reverse_word_index)
    #     train_X = keras.preprocessing.sequence.pad_sequences(train_X,
    #                                                          value=word_index["<PAD>"],
    #                                                          padding='post',
    #                                                          maxlen=256)
    #     test_X = keras.preprocessing.sequence.pad_sequences(test_X,
    #                                                          value=word_index["<PAD>"],
    #                                                          padding='post',
    #                                                          maxlen=256)
    #     vacab_size = 10000
    #     model = keras.Sequential()
    #     model.add(keras.layers.Embedding(vacab_size, 16, imput_shape=(None,)))
    #     model.add(keras.layers.GlobalAvgPool1D)
    #     model.add(keras.layers.Dense(16, activation=tf.nn.relu))
    #     model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))
    #     model.compile(optimizer=tf.optimizers.Adam(), loss='binary_crossentropy', metrics=['acc'])
    #     x_val = train_X[:10000]
    #     partial_X_train = train_X[10000:]
    #     y_val = train_Y[:10000]
    #     partial_Y_train = train_Y[10000:]
    #     history = model.fit(partial_X_train, partial_Y_train, epochs=40, batch_size=512, validation_data=(x_val, y_val))
    #     result = model.evaluate(test_X, test_Y)
    #     print(f'result :  {result}')
    #
    #     history_dict = history.history
    #     history_dict.keys()
    #     acc = history_dict['acc']
    #     val_acc = history_dict['val_acc']
    #     loss = history_dict['loss']
    #     val_loss = history_dict['val_loss']
    #     epochs = range(1, len(acc) + 1)
    #     print('==============')
    #     # "bo"는 "파란색 점"입니다
    #     plt.plot(epochs, loss, 'bo', label='Training loss')
    #     # b는 "파란 실선"입니다
    #     plt.plot(epochs, val_loss, 'b', label='Validation loss')
    #     plt.title('Training and validation loss')
    #     plt.xlabel('Epochs')
    #     plt.ylabel('Loss')
    #     plt.legend()

    def imdb_process(self):
        imdb = keras.datasets.imdb
        (train_X, train_y), (test_X, test_y) = imdb.load_data(num_words=10000)

        # test
        print('훈련용 리뷰 개수 : {}'.format(len(train_X)))
        print('테스트용 리뷰 개수 : {}'.format(len(test_X)))
        num_classes = len(set(train_y))
        print('카테고리 : {}'.format(num_classes))

        '''
        훈련용 리뷰 개수 : 25000
        테스트용 리뷰 개수 : 25000
        카테고리 : 2
        '''

        word_index = imdb.get_word_index()
        word_index = {k: (v + 3) for k, v in word_index.items()}
        word_index["<PAD>"] = 0
        word_index["<START>"] = 1
        word_index["<UNK>"] = 2  # Unknown
        word_index["<UNUSED>"] = 3
        revere_word_index = dict([(v, k) for (k, v) in word_index.items()])
        temp = self.decode_review(train_X[0], revere_word_index)
        train_X = keras.preprocessing.sequence.pad_sequences(train_X,
                                                             value=word_index['<PAD>'],
                                                             padding='post',
                                                             maxlen=256)
        test_X = keras.preprocessing.sequence.pad_sequences(test_X,
                                                            value=word_index['<PAD>'],
                                                            padding='post',
                                                            maxlen=256)
        vacab_size = 10000
        model = keras.Sequential()
        model.add(keras.layers.Embedding(vacab_size, 16, input_shape=(None,)))
        model.add(keras.layers.GlobalAvgPool1D())
        model.add(keras.layers.Dense(16, activation=tf.nn.relu))
        model.add(keras.layers.Dense(1, activation=tf.nn.sigmoid))  # 시그모이드를 쓰면 - 값까지 내려감, 긍 부부정을 사용하기 위해
        model.compile(optimizer=tf.optimizers.Adam(), loss='binary_crossentropy', metrics=['acc'])  # acc-accurcy
        x_val = train_X[:10000]
        partial_X_train = train_X[10000:]
        y_val = train_y[:10000]
        partial_y_train = train_y[10000:]
        history = model.fit(partial_X_train, partial_y_train, epochs=40, batch_size=512,
                            validation_data=(x_val, y_val))
        result = model.evaluate(test_X, test_y)
        print(f'result : {result}')

        '''
        result : [0.3362523913383484, 0.8712800145149231]
        '''

        history_dict = history.history
        history_dict.keys()
        acc = history_dict['acc']
        val_acc = history_dict['val_acc']
        loss = history_dict['loss']
        val_loss = history_dict['val_loss']
        epochs = range(1, len(acc) + 1)
        print('==============')
        # "bo"는 "파란색 점"입니다
        plt.plot(epochs, loss, 'bo', label='Training loss')
        # b는 "파란 실선"입니다
        plt.plot(epochs, val_loss, 'b', label='Validation loss')
        plt.title('Training and validation loss')
        plt.xlabel('Epochs')
        plt.ylabel('Loss')
        plt.legend()


        plt.clf()  # 그림을 초기화합니다

        plt.plot(epochs, acc, 'bo', label='Training acc')
        plt.plot(epochs, val_acc, 'b', label='Validation acc')
        plt.title('Training and validation accuracy')
        plt.xlabel('Epochs')
        plt.ylabel('Accuracy')
        plt.legend()
        plt.savefig(f'{self.vo.context}show_npl.png')




class NaverMovie(object):
    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/nlp/data/'

    def web_scraping(self):
        ctx = self.vo.context
        driver = webdriver.Chrome(f'{ctx}chromedriver')
        driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_divs = soup.find_all('div', attrs={'class', 'tit3'})
        # products = [[div.a.string for div in all_divs]]  #  list [] 타입 -> matrix [[]] 타입으로 변경  / csv 분석 : https://docs.python.org/ko/3/library/csv.html
        '''
        [['듄', '베놈 2: 렛 데어 비 카니지', '라스트 듀얼: 최후의 결투', '007 노 타임 투 다이', '노회찬6411', '이터널스', '고양이를 부탁해', '보이스', '휴가', '모가디슈', '기적', '십개월의 미래', '수색자', '아네트', '브라더', '당신얼굴 앞에
        서', '코다', '강릉', '용과 주근깨 공주', '고장난 론', '할로윈 킬즈', '요시찰', '스틸워터', '극장판 짱구는 못말려: 격돌! 낙서왕국과 얼추 네 명의 용사들', '애프터: 관계의 함정', '인질', '화이트데이: 부서진 결계', '한창나이 선녀님', '
        귀멸의 칼날: 남매의 연', '가을의 전설', '프리 가이', '동백', '경고', '샹치와 텐 링즈의 전설', '첫눈이 사라졌다', '스파이더맨: 노 웨이 홈', '장르만 로맨스', '당신은 믿지 않겠지만', '그래비티', '쁘띠 마망', '체리 향기', '타다: 대한민
        국 스타트업의 초상', '푸른 호수', '올드', '밥정', '가족의 색깔', '그린 북', '킬링 카인드 ', '사상', '싱크홀']]
        '''

        # var 1
        # f = open(f'{ctx}naver_movie_dataset_0.csv', 'w', encoding='UTF-8', newline='')
        # for product in products:
        #     wr = csv.writer(f, delimiter=',')
        #     wr.writerow(product)

        # var 2
        with open(f'{ctx}naver_movie_dataset_1.csv', 'w', encoding='UTF-8', newline='') as f:
            # for product in products:  # 굳이 필요 하지 않음.
            # wr = csv.writer(f, delimiter=',')  # csv 분석 : https://docs.python.org/ko/3/library/csv.html
            wr = csv.writer(f)  # 한줄 프린트 필요
            # wr.writerows(products)  # writerow : 1차원 list에 대한 row를 저장하는데 사용 # writerows : 2차원 list에 대한 row를 저장하는데 사용
            wr.writerows([[div.a.string for div in all_divs]])
            print([[div.a.string for div in all_divs]])

        # var 3
        # for product in products:
        #     with open(f'{ctx}naver_movie_dataset_2.csv', 'w', encoding='UTF-8', newline='') as f:
        #         wr = csv.writer(f, delimiter=',')
        #         wr.writerows(product)

        driver.close()

    def naver_process(self):
        # self.web_scraping()
        corpus = pd.read_table(f'{self.vo.context}naver_movie_dataset.csv', sep=',', encoding='UTF-8')
        train_X = np.array(corpus)
        # 카테고리 0 (긍정) 1 (부정)
        n_class0 = len([1 for _, point in train_X if point > 3.5])
        n_class1 = len([train_X]) - n_class0
        counts = defaultdict(lambda : [0, 0])   # defaultdict : 팩토리 ->dict 생성  #  초기화 시킴
        for doc, point in train_X:
            if self.isNumber(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 3.5 else 1] += 1
        word_counts = counts
        print(f'word_counts ::: {word_counts}')
        '''
        word_counts ::: defaultdict(<function NaverMovie.naver_process.<locals>.<lambda> at 0x000002C0ED2BD550>, {})
        '''

    def isNumber(self, doc):  # try : float 밖에 두어야 하는 이유?
        try:
            float(doc)
            return True
        except ValueError:
            return False


    def load_corpus(self, fname):
        pass

    def count_words(self, train_X):
        pass

