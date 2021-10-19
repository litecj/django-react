import numpy as np
from django.db import models

import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow import keras
# Create your models here.
from admin.common.models import ValueObject


class FashionClassification(object):

    def fashion(self): # 함수형
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=[28, 28]),
            keras.layers.Dense(400, activation="relu"),
            keras.layers.Dense(200, activation="relu"),
            keras.layers.Dense(200, activation="relu"),
            keras.layers.Dense(10, activation="softmax")
        ])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        model.fit(train_images, train_labels, epochs=5)
        test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)  # verbose 는 학습하는 내부상황 보기 중 2번선택
        predictions = model.predict(test_images)
        i = 13
        print(f'모델이 예측한 값 {np.argmax(predictions[i])}')
        print(f'정답: {test_labels[i]}')
        print(f'테스트 정확도: {test_acc}')
        plt.figure(figsize=(6, 3))
        plt.subplot(1, 2, 1)
        test_image, test_predictions, test_label = test_images[i], predictions[i], test_labels[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(test_image, cmap=plt.cm.binary)
        test_pred = np.argmax(test_predictions)
        print(f'{test_pred}')
        print('#' * 100)
        print(f'{test_label}')

        if test_pred == test_label:
            color = 'blue'
        else:
            color = 'red'
        plt.xlabel('{} : {} %'.format(self.class_name[test_pred],
                                      100 * np.max(test_predictions),
                                      self.class_name[test_label], color))
        plt.subplot(1, 2, 2)
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        this_plot = plt.bar(range(10), test_pred, color='#777777')
        plt.ylim([0, 1])
        test_pred = np.argmax(test_predictions)
        this_plot[test_pred].set_color('red')
        this_plot[test_label].set_color('blue')
        plt.savefig(f'{self.vo.context}fashion_answer(13).png')

    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/tensor/data/'
        self.class_name = ['T-shirt/top', 'Trouser', 'Pullover', 'Dress', 'Coat',
                           'Sandal', 'Shirt', 'Sneaker', 'Bag', 'Ankle boot']

    def hook(self):
        [train_images, train_labels, test_images, test_labels] = self.get_data()
        model = self.create_model()
        model.fit(train_images, train_labels, epochs=5)
        test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2) # verbose 는 학습하는 내부상황 보기 중 2번선택
        predictions = model.predict(test_images)
        i = 7
        print(f'모델이 예측한 값 {np.argmax(predictions[i])}')
        print(f'정답: {test_labels[i]}')
        print(f'테스트 정확도: {test_acc}')
        plt.figure(figsize=(6,3))
        plt.subplot(1,2,1)
        test_image, test_predictions, test_label = test_images[i], predictions[i], test_labels[i]
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        plt.imshow(test_image, cmap=plt.cm.binary)
        test_pred = np.argmax(test_predictions)
        print(f'{test_pred}')
        print('#'*100)
        print(f'{test_label}')

        if test_pred == test_label:
            color = 'blue'
        else:
            color = 'red'
        plt.xlabel('{} : {} %'.format(self.class_name[test_pred],
                                     100 * np.max(test_predictions),
                                     self.class_name[test_label], color))
        plt.subplot(1, 2, 2)
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        this_plot = plt.bar(range(10), test_pred, color='#777777')
        plt.ylim([0, 1])
        test_pred = np.argmax(test_predictions)
        this_plot[test_pred].set_color('red')
        this_plot[test_label].set_color('blue')
        plt.savefig(f'{self.vo.context}fashion_answer.png')


    def process(self):
        self.hook()


    def get_data(self) -> []:
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
        # self.peek_datas(X_train_full, X_test, y_train_full)
        '''
        print(f'X_train_full.shape : \n {X_train_full.shape}')
        print(f'X_train_full.dtype : \n {X_train_full.dtype}')
        print(f'train 행 :  {X_train_full.shape[0]} \n train 열 : {X_train_full.shape[1]}')
        print(f'test 행 :  {X_test.shape[0]} \n test 열 : {X_test.shape[1]}')
        X_train_full.shape : (60000, 28, 28)
        X_train_full.dtype : uint8
        train 행 :  60000 / train 열 : 28
        test 행 :  10000 / test 열 : 28
        '''
        # plt.figure()
        # plt.imshow(X_train_full[3])
        # plt.colorbar()
        # plt.grid(False)
        # plt.savefig(f'{self.vo.context}fashion_random.png')

        return [train_images, train_labels, test_images, test_labels]

    def peek_datas(self, train_images, test_images, train_labels):
        print(train_images.shape)
        print(train_images.dtype)
        print(f'훈련 행: {train_images.shape[0]} 열: {train_images.shape[1]}')
        print(f'테스트 행: {test_images.shape[0]} 열: {test_images.shape[1]}')
        plt.figure()
        plt.imshow(train_images[3])
        plt.colorbar()
        plt.grid(False)
        plt.savefig(f'{self.vo.context}fashion_random.png')
        plt.figure(figsize=(10, 10))
        for i in range(25):
            plt.subplot(5, 5, i + 1)
            plt.xticks([])
            plt.yticks([])
            plt.grid(False)
            plt.imshow(train_images[i], cmap=plt.cm.binary)
            plt.xlabel(self.class_name[train_labels[i]])
        plt.savefig(f'{self.vo.context}fashion_subplot.png')


    def create_model(self) -> object:
        '''
        model = keras.Sequential()
        model.add(keras.layers.Flatten(input_shape=[28, 28])) # matrx (X - 대문자 x) / 입력층
        model.add(keras.layers.Dense(300, activation="relu")) # neron count 300 / 은닉층
        model.add(keras.layers.Dense(100, activation="relu")) # neron count 100
        model.add(keras.layers.Dense(10, activation="softmax")) # 출력층 활성화 함수는 "softmax" / count 10
        '''
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=[28, 28]),
            # keras.layers.Dense(128, activation=tf.nn.relu),
            keras.layers.Dense(128, activation="relu"),
            keras.layers.Dense(10, activation="softmax")
        ])
        # model.complie(loss="sparse_categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])
        model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])
        # sgd 보다 adam 이 더 신상
        return model

    def train_model(self, model, train_images, train_labels) -> object:
        model.fit(train_images, train_labels, epochs=5) # epochs=5 5회전 -> fit 은 for 돌리는 느낌?

    def test_model(self, model, test_images, test_labels) -> object:
        test_loss, test_acc = model.evaluate(test_images, test_labels)  # evaluate : 평가하는 것 (test_images: 문제 , test_labels: 답 주고 평가하는 것)
        print('Test accuracy:', test_acc)

    def predict(self, model, test_images, test_labels, index):
        prediction = model.predict(test_images)
        pred = prediction[index]
        answer = test_labels[index]
        print(f' 모델이 예측한 값 : \n {np.argmax(pred)}')
        print(f'정답 : \n {answer}')
        # np.argmax(prediction[0])
        return [prediction, test_images, test_labels]

    def plot_image(self):
        pass

    def plot_value_array(self):
        pass

    def fit(self):
        pass






class AdalineGD(object): # 적응형 선형 뉴런 분류기

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        # X : {array-like}, shape = [n_samples, n_features]
        #           n_samples 개의 샘플과 n_features 개의 특성으로 이루어진 훈련 데이터

        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.cost_ = [] # 에포크마다 누적된 비용 함수의 제곱합

        for i in range(self.n_iter):
            net_input = self.net_input(X)
            # Please note that the "activation" method has no effect
            # in the code since it is simply an identity function. We
            # could write `output = self.net_input(X)` directly instead.
            # The purpose of the activation is more conceptual, i.e.,
            # in the case of logistic regression (as we will see later),
            # we could change it to
            # a sigmoid function to implement a logistic regression classifier.
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (errors**2).sum() / 2.0
            self.cost_.append(cost)
        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, X):
        return X

    def predict(self, X): # 단위 계단 함수를 사용하여 클래스 레이블을 반환
        return np.where(self.activation(self.net_input(X)) >= 0.0, 1, -1)



class Perceptron(object):

    '''
    매개변수
    eta : float 학습률(0.0과 1.0 사이 : 스케일러)
    n_iter : int 훈련 데이터셋 반복 횟수
    random_state : int 가중치 무작위 초기화를 위한 난수 생성기기
   '''
    # 2차 함수로 넘기는 순간, 그래픽, 비선형 구조이기에 이터레이터 밖에 안됨 . 이너레이터 불가

    '''
    속성
    w_ : 1d-array : 학습된 가중치
    errors_ : list 에포크마다 누적된 분류 오류
    '''

    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def process(self):
        pass

    def fit(self, X, y) -> object: # 훈련데이터 학습 ( y = WX + b)
        # X 대문자 사용 이유 : 값이 늘 메트리스 구조 이기 때문 -> 한개의 값이 아닌 여러개의 값이기 때문이다.
        # y 소문자 사용 이유 : 늘 값이 한개만 되어야 하기 때문
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1+X.shape[1])
        # scale=0.01 = 1/100, 100번 교육 시키겠다.
        self.errors_ = []

        # 매트리스 구조이기에 이중 for문 필요
        for _ in range(self.n_iter):
            errors = 0  # errors  오차
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi))
                self.w_[1:] += update * xi
                self.w_[0] += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    # 단위 계산 함수를 사용하여 클래스 레이블 반환
    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, -1)

    # 최종 입력 계산
    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]








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
        # x2 = tf.reshape(x_array, shape=(3, 2, 3))
        x2 = tf.reshape(x_array, shape=(-1, 6))
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