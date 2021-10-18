import numpy as np
from django.db import models

import tensorflow as tf


# Create your models here.

class Perceptron(object):
    def __init__(self):
        pass

    def process(self):
        pass












class Calculator(object):

    def __init__(self):
        # print(f'Tensorflow Version{tf.__version__}')  # Tensorflow Version2.6.0
        pass

    def process(self):
        self.plus(100132, 726062)
        print('*'*100)
        self.mean()

    def plus(self, a, b):
        print(tf.constant(a)+tf.constant(b))

    def mean(self):
        x_array = np.arange(18).reshape(3, 2, 3)
        x2 = tf.reshape(x_array, shape=(3, 2, 3))
        # x2 = tf.reshape(x_array, shape=(-1, 6))
        # 각 열의 합을 계산
        xsum = tf.reduce_sum(x2, axis=0)
        # 각 열의 평균을 계산
        xmean = tf.reduce_mean(x2, axis=0)

        print(f'입력 크기 : \n {x_array.shape}\n')
        print(f'크기가 변경된 입력 크기 :\n {x2.numpy()}\n')
        print(f'열의 합 : \n {xsum.numpy()}\n')
        print(f'열의 평균 : \n {xmean.numpy()}\n')


        '''
            함수	설명
            tf.add	덧셈
            tf.subtract	뺄셈
            tf.multiply	곱셈
            tf.div	나눗셈의 몫(Python 2 스타일)
            tf.truediv	나눗셈의 몫(Python 3 스타일)
            tf.mod	나눗셈의 나머지
            tf.abs	절대값을 리턴합니다.
            tf.negative	음수를 리턴합니다.
            tf.sign	부호를 리턴합니다.(역주: 음수는 -1, 양수는 1, 0 일땐 0을 리턴합니다)
            tf.reciprocal	역수를 리턴합니다.(역주: 3의 역수는 1/3 입니다)
            tf.square	제곱을 계산합니다.
            tf.round	반올림 값을 리턴합니다.
            tf.sqrt	제곱근을 계산합니다.
            tf.pow	거듭제곱 값을 계산합니다.
            tf.exp	지수 값을 계산합니다.
            tf.log	로그 값을 계산합니다.
            tf.maximum	최대값을 리턴합니다.
            tf.minimum	최소값을 리턴합니다.
            tf.cos	코사인 함수 값을 계산합니다.
            tf.sin	사인 함수 값을 계산합니다.
        '''