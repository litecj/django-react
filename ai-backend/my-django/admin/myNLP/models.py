from django.db import models

# Create your models here.
from admin.common.models import ValueObject

from math import log, exp
from collections import defaultdict
import numpy as np
from admin.common.models import ValueObject
import pandas as pd

class NaverMovie(object):

    def __init__(self):
        self.vo = ValueObject()
        self.vo.context = 'admin/myNLP/data/'
        self.k = 0.5
        self.word_probs = []

    def naver_process(self):
        n = NaverMovie()
        n.model_fit()
        result = n.classify('내 인생 최고의 영화')  # 0.9634566316047457
        print(f'결과 :::: {result}')
        result = n.classify('시간 아깝다. 정말 쓰레기다')  # 0.00032621763187734896
        print(f'결과 :::: {result}')
        result = n.classify('평범하다, 배우들 연기가 아쉽다')  # 0.6595745160614442
        print(f'결과 :::: {result}')
        result = n.classify('지루했다')  # 0.01367458951253406
        print(f'결과 :::: {result}')
        print('#'*100)

    def load_corpus(self):
        corpus = pd.read_table(f'{self.vo.context}review_train.csv', sep=',', encoding='UTF-8')
        corpus = np.array(corpus)
        return corpus

    def count_words(self, train_X):
        counts = defaultdict(lambda: [0, 0])
        for doc, point in train_X:
            if self.isNumber(doc) is False:
                words = doc.split()
                for word in words:
                    counts[word][0 if point > 3.5 else 1] += 1
        return counts


    def isNumber(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False


    def word_probabilities(self, counts, n_class0, n_class1, k):
        return [(w,
                 (class0 + k) / (n_class0 + 2 * k),
                 (class1 + k) / (n_class1 + 2 * k))
                for w, (class0, class1) in counts.items()]


    def probability(self, word_probs, doc):
        docwords = doc.split()
        log_prob_if_class0 = log_prob_if_class1 = 0.0
        for word, prob_if_class0, prob_if_class1 in word_probs:
            if word in docwords:
                log_prob_if_class0 += log(prob_if_class0)
                log_prob_if_class1 += log(prob_if_class1)
            else:
                log_prob_if_class0 += log(1.0 - prob_if_class0)
                log_prob_if_class1 += log(1.0 - prob_if_class1)
        prob_if_class0 = exp(log_prob_if_class0)
        prob_if_class1 = exp(log_prob_if_class1)
        return prob_if_class0 / (prob_if_class0 + prob_if_class1)


    def model_fit(self):
        train_X = self.load_corpus()
        '''
        '재밋었네요': [1, 0]
        '별로재미없다': [0, 1]
        '''
        num_class0 = len([1 for _, point in train_X if point > 3.5])
        num_class1 = len(train_X) - num_class0
        word_counts = self.count_words(train_X)
        self.word_probs = self.word_probabilities(word_counts, num_class0, num_class1, self.k)

    def classify(self, doc):
        return self.probability(self.word_probs, doc)