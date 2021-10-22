from django.db import models
import math
import pandas_datareader as data_reader
import numpy as np
from tqdm import tqdm
import numpy as np
import tensorflow as tf
from collections import deque
import random

# Create your models here.
from admin.common.models import ValueObject


class AITrader(object):

    def __init__(self, action_space=3, model_name='AITrader'):
        self.vo = ValueObject()
        self.vo.context = 'admin/ai_trader/data/'

        self.state_size = 10 # windows size
        self.action_space = action_space
        self.memory = deque(maxlen=2000)
        self.inventory = []
        self.model_name = model_name
        self.gamma = 0.95
        self.epsilon = 1.0
        self.epsilon_final = 0.01
        self.epsilon_decay = 0.995
        self.model = self.model_builder()

    def process(self):
        Trading().transaction('AAPL')


    def model_builder(self):
        model = tf.keras.models.Sequential([
            tf.keras.layers.Dense(units=32, activation="relu", input_dim=self.state_size),
            # tf.keras.layers.Dropout(rate=0.2),
            tf.keras.layers.Dense(units=64, activation="relu"),
            # tf.keras.layers.Dropout(rate=0.2),
            tf.keras.layers.Dense(units=128, activation="relu"),
            # tf.keras.layers.Dropout(rate=0.2),
            tf.keras.layers.Dense(units=self.action_space, activation="linear"),
            # tf.keras.layers.Dropout(rate=0.2),
            tf.keras.layers.Dense(1, activation="softmax")
        ])

        model.compile(loss='mse', optimizer = tf.keras.optimizers.Adam(lr=0.001))
        # model.save(f'{self.vo.context}test_data/ai_trader.h5')

        return model

        # model = tf.keras.models.Sequential()
        # model.add(tf.keras.layers.Dense(units=32, activation="relu", input_dim=self.state_size))
        # model.add(tf.keras.layers.Dropout(rate=0.2))
        # model.add(tf.keras.layers.Dense(units=64, activation="relu"))
        # model.add(tf.keras.layers.Dropout(rate=0.2))
        # model.add(tf.keras.layers.Dense(units=128, activation="relu"))
        # model.add(tf.keras.layers.Dropout(rate=0.2))
        # model.add(tf.keras.layers.Dense(units=self.action_space, activation="linear"))
        # model.add(tf.keras.layers.Dropout(rate=0.2))
        # model.add(tf.keras.layers.Dense(units=1, activation="softmax"))
        #
        # model.compile(loss='mse', optimizer=tf.keras.optimizer.Adam(lr=0.001))
        # model.save(f'{self.vo.context}test_data/ai_trader.h5')

    def trade(self, state):
        # model = tf.keras.models.load_model(f'{self.vo.context}test_data/ai_trader.h5')
        if random.random() <= self.epsilon:
            return random.randrange(self.action_space)
        actions = self.model.predict(state)
        return np.argmax(actions[0])


    def batch_train(self, batch_size):
        model = self.model
        batch = []
        for i in range(len(self.memory) - batch_size +1, len(self.memory)):
            batch.append(self.memory[i])

        for state, action, reward, next_state, done in batch:
            print(f'################# batch_train 1 ################# {action}')
            reward = reward
            if not done:
                reward = reward + self.gamma * np.amax(model.predict(next_state)[0])
            target = model.predict(state)
            print(f'################# batch_train 1 action ################# {action}')
            target[0][action] = reward
            model.fit(state, target, epochs=1, verbose=0)
        if self.epsilon > self.epsilon_final:
            self.epsilon *= self.epsilon_decay


class Trading:
    def __init__(self):
        pass

    def sigmoid(self, x):
        return 1 / (1 +math.exp(-x))

    def stock_price_format(self, n):
        if n < 0:
            return "- $ {0:2f}".format(abs(n))
        else:
            return "$ {0:2f}".format(abs(n))

    def dataset_loader(self, stock_name):

        dataset = data_reader.DataReader(stock_name, data_source='yahoo')
        start_date = str(dataset.index[0]).split()[0]
        end_date = str(dataset.index[-1]).split()[0]
        close = dataset['Close']
        return close

    def state_creator(self, data, timestep, window_size):
        starting_id = timestep - window_size +1
        if starting_id >= 0:
            windowed_data = data[starting_id: timestep +1]
        else:
            windowed_data =- starting_id * [data[0]] + list(data[0:timestep +1])

        state = []
        for i in range(window_size - 1):
            state.append(self.sigmoid(windowed_data[i+1] - windowed_data[i]))
        return np.array([state])

    def transaction(self, stock_name):

        data = self.dataset_loader(stock_name)

        window_size = 10
        epdisodes = 100  # 거래 하는 횟수, 많이 하면 할 수록 똑똑해짐
        batch_size = 32
        data_samples = len(data) -1
        trader = AITrader(window_size)
        for episode in range(1, epdisodes+1):
            print(f'Episode:   {episode}/{epdisodes}')
            state = self.state_creator(data, 0, window_size+1)
            total_profit = 0
            trader.inventory = []

            for t in tqdm(range(data_samples)):
                action = trader.trade(state)
                next_state = self.state_creator(data, t+1, window_size+1)
                reward = 0
                if action == 1: #Buying
                    trader.inventory.append(data[t])
                    print(f' AI 트레이더 매수 : {self.stock_price_format(data[t])}')
                elif action == 2 and len(trader.inventory) > 0:
                    buy_price = trader.inventory.pop(0)
                    reward = max(data[t] - buy_price, 0)
                    total_profit += data[t] - buy_price
                    print("AI 트레이더 매도: ", self.stock_price_format(data[t]),
                          "이익: "+self.stock_price_format(data[t] - buy_price))
                if t == data_samples -1 :
                    done = True
                else:
                    done = False
                trader.memory.append((state, action, reward, next_state, done))
                state = next_state

                if done:
                    print('#####################################')
                    print(f'총이익: {total_profit}')
                    print('#####################################')

                if len(trader.memory) > batch_size:
                    trader.batch_train(batch_size)

            if episode % 100 == 0:
                trader.model.save(f'{self.vo.context}ai_trader_{episode}.h5')
