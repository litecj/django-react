from django.db import models
import pandas as pd
import os
import matplotlib.pyplot as plt
import mglearn
import numpy as np

from sklearn.tree import DecisionTreeRegressor
from sklearn.linear_model import LinearRegression

# Create your models here.
from admin.common.models import ValueObject, Reader


class MyRNN(object):

    def __init__(self):
        self.vo = ValueObject()
        self.reader = Reader()
        self.vo.context = 'admin/rnn/data/'

    def ram_price(self):
        ram_price = pd.read_csv(os.path.join(mglearn.datasets.DATA_PATH, "ram_price.csv"))
        plt.semilogy(ram_price.date, ram_price.price)
        plt.xlabel("년")
        plt.ylabel("가격")
        # plt.savefig(f'{self.vo.context}test_data/ram_price.png')
        train = ram_price[ram_price['date'] < 2000]  # 2000년 이전 기준
        test = ram_price[ram_price['date'] >= 2000]  # 2000년 이후 기준
        x_train = train['date'][:, np.newaxis]
        y_train = np.log(train['price'])
        tree = DecisionTreeRegressor().fit(x_train, y_train)
        lr = LinearRegression().fit(x_train, y_train)
        x_all = ram_price['date'].values.reshape(-1, 1)
        pred_tree = tree.predict(x_all)
        price_tree = np.exp(pred_tree)  # log 값 되돌리기
        pred_lr = lr.predict(x_all)
        price_lr = np.exp(pred_lr)  # log 값 되돌리기

        #####
        plt.semilogy(ram_price['date'], pred_tree,
                     label="TREE PREDIC", ls='-', dashes=(2, 1))
        plt.semilogy(ram_price['date'], pred_lr,
                     label="LINEAR REGRESSION PREDIC", ls=':')
        plt.semilogy(train['date'], train['price'], label='TRAIN DATA', alpha=0.4)
        plt.semilogy(test['date'], test['price'], label='TEST DATA')
        plt.legend(loc=1)
        plt.xlabel('year', size=15)
        plt.ylabel('price', size=15)
        plt.savefig(f'{self.vo.context}test_data/ram_price_prediction.png')