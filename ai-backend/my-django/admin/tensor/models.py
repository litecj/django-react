import numpy as np
from django.db import models

import tensorflow as tf
from matplotlib import pyplot as plt
from tensorflow import keras
# Create your models here.
from admin.common.models import ValueObject


class TensorFunction(object):  # python: 객체는 빈통, 객체 안에 데이터를 넣으면 모델 / Java : 인스턴스는 빈통
    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/tensor/data/'

    def hook(self):
        menu = 'create_model_summary'
        if menu == 'tf_function' :
            result = self.tf_function()

        elif menu == 'tf_sum':
            result = self.decorator_example()

        elif menu == 'tf_add':
            result = self.tf_add()

        elif menu == 'tf_multiply':
            result = self.gugu2(2)

        elif menu == 'create_model':
            result = self.create_model()

        elif menu == 'create_model_summary':
            result = self.create_model().summary()

        else:
            result = '해당사항 없음'

        print(f'결과 : {result}')


        # self.tf_function()
        # self.gugu2(2)
        # print(f'self.gugu2(2) : {self.gugu2(2)}')
        # print(self.gugu2(2))
        # print(f'결과 : {self.decorator_example()}')
        # print(self.decorator_example())
        # self.decorator_example()

    # 구구단
    @tf.function
    def gugu2(self, dan):
        for i in range(1, 10):
            result = tf.multiply(dan, i)
            # print(result.numpy()) # AttributeError: 'Tensor' object has no attribute 'numpy'
            print(result)
        return result

    def tf_add(self):
        x = [1, 2, 3, 4, 5]
        y = 2 # 하나의 경우는 모든 요소의 값에 연결 됨
        # y =[2, 3] # 양 값의 방향이 맞지 않으면 안됨 -> 같은 인덱스 끼리만 하기 때문이다.
        y = [4, 5, 6, 7, 8] # 양 방향의 값이 같으면 계산이 가능하다.
        z = tf.add(x, y)
        z = tf.multiply(x, y)
        z = tf.subtract(x, y)
        z = tf.divide(x, y)
        return z

    def make_random_data(self):
        x = np.random.uniform()

    def create_model(self)-> object:
        input = tf.keras.Input(shape=(1,))
        output = tf.keras.layers.Dense(1)(input)
        model = tf.keras.Model(input, output)
        return model

    '''
        Model: "model" = tensorflow  의 구조조
       _________________________________________________________________
        Layer (type)                 Output Shape              Param #
        =================================================================
        input_1 (InputLayer)         [(None, 1)]               0
        _________________________________________________________________
        dense (Dense)                (None, 1)                 2
        =================================================================
        Total params: 2
        Trainable params: 2
        Non-trainable params: 0
        _________________________________________________________________
        결과 : None
    '''

    @tf.function  # tensorflow's function : 본질의 변화는 없으나, 데코레이터 된거임
    def decorator_example(self):
        a = tf.constant(1, tf.float32)  # tensorflow 의 변수는 내장 된 것만 가능. 외부에서 받는 건 모두 상수 이다
        b = tf.constant(2, tf.float32)
        c = tf.constant(3, tf.float32)
        z = a + b + c
        print(f'@tf.function 사용하기 z : {z}')
        # z1 = tf.add(a, b, c)
        print(f'a : {a}, b : {b}, c: {c}')
        # print(f'@tf.function 사용하기 z1 : {z1}')
        return z

    # Not tensorflow's function
    def tf_function(self):
        mnist = tf.keras.datasets.mnist
        (X_train, y_train), (X_test, y_test) = mnist.load_data()
        X_train, X_test = X_train / 255.0, X_test /255.0
        X_train = X_train[..., tf.newaxis]  # [행 , 열]  # 행의 추가 = 차원 추가
        X_test = X_test[..., tf.newaxis]
        train_ds = tf.data.Dataset.from_tensor_slices((X_train, y_train)).shuffle(10000).batch(32)
        test_ds =  tf.data.Dataset.from_tensor_slices((X_test, y_test)).batch(32)

        # print(f'train_ds : {type(train_ds)}')
        '''
        train_ds : <class 'tensorflow.python.data.ops.dataset_ops.BatchDataset'>
        '''
        # print(list(train_ds.as_numpy_iterator())) # 너무 길게 나옴
        return train_ds.as_numpy_iterator()

class FashionClassification(object):

    def fashion(self): # 함수형
        fashion_mnist = keras.datasets.fashion_mnist
        (train_images, train_labels), (test_images, test_labels) = fashion_mnist.load_data()
        # self.peek_datas(train_images, test_images, test_labels)
        model = keras.Sequential([
            keras.layers.Flatten(input_shape=[28, 28]),
            keras.layers.Dense(400, activation="relu"),  # neron count 128
            keras.layers.Dense(128, activation="relu"),
            keras.layers.Dense(128, activation="relu"),
            keras.layers.Dense(10, activation="softmax")  # 출력층 활성화함수는 softmax
        ])
        model.compile(optimizer='adam',
                      loss='sparse_categorical_crossentropy',
                      metrics=['accuracy'])
        model.fit(train_images, train_labels, epochs=5)

        # 확인 및 테스트 완료 후, 프로그램 저장
        model.save(f'{self.vo.context}my_keras_model.h5')
        # 이후 사용을 위한, 프로그램 사용을 위한 호출
        model = keras.models.load_model("my_keras_model.h5")


        # 확인 및 테스트를 위한 절차
        '''
        test_loss, test_acc = model.evaluate(test_images, test_labels, verbose=2)  # verbose 는 학습하는 내부상황 보기 중 2번선택
        predictions = model.predict(test_images)
        i = 9
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

        if test_pred == test_label:
            color = 'blue'
        else:
            color = 'red'
        plt.xlabel('{} : {} %'.format(self.class_names[test_pred],
                                      100 * np.max(test_predictions),
                                      self.class_names[test_label], color))
        plt.subplot(1, 2, 2)
        plt.grid(False)
        plt.xticks([])
        plt.yticks([])
        this_plot = plt.bar(range(10), test_pred, color='#777777')
        plt.ylim([0, 1])
        test_pred = np.argmax(test_predictions)
        this_plot[test_pred].set_color('red')
        this_plot[test_label].set_color('blue')
        plt.savefig(f'{self.vo.context}fashion_answer(9).png')
        '''

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