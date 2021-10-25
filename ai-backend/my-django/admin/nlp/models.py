
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

    def naver_process(self):
        ctx = self.vo.context
        driver = webdriver.Chrome(f'{ctx}chromedriver')
        driver.get('https://movie.naver.com/movie/sdb/rank/rmovie.naver')
        soup = BeautifulSoup(driver.page_source, 'html.parser')
        all_divs = soup.find_all('div', attrs={'class', 'tit3'})
        products = [div.a.string for div in all_divs]

        # f = open(f'{ctx}naver_movie_dataset_0.csv', 'w', encoding='UTF-8', newline='')
        # for product in products:
        #     wr = csv.writer(f, delimiter=',')
        #     wr.writerow(product)

        with open(f'{ctx}naver_movie_dataset_3.csv', 'w', encoding='UTF-8', newline='') as f:
            for product in products:
                wr = csv.writer(f, delimiter=',')
                wr.writerow(product)  # writerows : 세로 정렬  # writerow : 가로 정렬
                print(product)

        # for product in products:
        #     with open(f'{ctx}naver_movie_dataset_2.csv', 'w', encoding='UTF-8', newline='') as f:
        #         wr = csv.writer(f, delimiter=',')
        #         wr.writerows(product)

        driver.close()


