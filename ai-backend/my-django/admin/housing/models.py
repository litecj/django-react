import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from django.db import models

# Create your models here.
from icecream import ic
from sklearn.model_selection import train_test_split, StratifiedShuffleSplit

from admin.common.models import DFrameGenerator


class HousingService(object):

    # def __init__(self, train_set, test_set): # 처음 시도 시, test와 train 형성하여 사용
    #     self.train_set = train_set
    #     self.test_set = test_set

    def __init__(self): # HousingService 사용시 자동으로 데이터프레임 생성
        self.dfg = DFrameGenerator()
        self.dfg.fname = 'admin/housing/data/housing.csv'
        self.model = self.dfg.create_model()

    def housing_info(self):
        self.dfg.model_info(self.model)

    # def new_model(self)-> object:  # "object"는 데이터프레임 / pd는 소문자지만 매서드  ↑ 'init'에서 'self.dfg.fname'과정으로 해결
    #     return pd.read_csv(self.dfg.fname)

    def housing_hist(self)-> object:
        self.model.hist(bins=50, figsize=(20, 15))
        plt.savefig('admin/housing/image/housing_hist.png')

    # def housing_info(self, model): # views에서 하던거 함수로 한번에 호출하고자 정리 -> common으로 옮김 (계속 사용 할 가능성 高)
    #     ic(model.head(3))
    #     ic(model.tail(3))
    #     ic(model.info())
    #     ic(model.describe())

    def split_model(self)->[]:  # 그냥 임의로 값을 나눈 것 / train_test_split = 함수(앞이 소문자)
        train_set, test_set = train_test_split(self.model, test_size=0.2, random_state=42) # 'self.model'에서 42(난수 초기값)를 기준으로 20%
        print('*' * 100)
        self.dfg.model_info(train_set)
        print('#' * 100)
        self.dfg.model_info(test_set)
        return [train_set, test_set]
        # self.train_set, self.test_set = train_test_split(self.new_model(), test_size=0.2, random_state=42)
        # return train_test_split(self.new_model(), test_size=0.2, random_state=42)


    def income_cat_hist(self): #cat = 카테고리
        h = self.model
        h['income_cat'] = pd.cut(h['median_income'], # median = 평균 X, 중간값
                                 bins=[0.,1.5,3.0,4.5,6.,np.inf], # np.inf is NaN(Not a Numer) / 0. = 정수를 의미함
                                 labels = [1,2,3,4,5]
                                 )
        h['income_cat'].hist()
        plt.savefig('admin/housing/image/income-cat.png')

    def split_model_by_income_cat(self) -> []:  # 'income_cat'을 기준으로 나눈 것 / StratifiedShuffleSplit = 생성자(매서드(앞에 대문자))
        h = self.model

        # 'income_cat'에 대한 key 형성 없어서 에러
        # h['income_cat'] = pd.cut(h['median_income'], # median = 평균 X, 중간값
        #                          bins=[0.,1.5,3.0,4.5,6.,np.inf], # np.inf is NaN(Not a Numer) / 0. = 정수를 의미함
        #                          labels = [1,2,3,4,5]
        #                          )

        split = StratifiedShuffleSplit(n_splits=1, test_size=0.2, random_state=42)
        for train_idx, test_idx in split.split(h, h['income_cat']):
            temp_train_set = h.loc[train_idx]
            temp_test_set = h.loc[test_idx]
        ic(temp_test_set['income_cat'].value_counts() / len(temp_test_set))
        ic(temp_train_set['income_cat'].value_counts() / len(temp_train_set))


class Housing(models.Model):

    # use_in_migrations = True
    id = models.AutoField(primary_key=True)
    longitude = models.FloatField()
    latitude = models.FloatField()
    housing_median_age = models.FloatField()
    total_rooms = models.FloatField()
    total_bedrooms = models.FloatField()
    population = models.FloatField()
    households = models.FloatField()
    median_income = models.FloatField()
    median_house_value = models.FloatField()
    ocean_proximity = models.TextField()

    class Meta:
        db_table = "housing"

    def __str__(self):
        return f'[{self.pk}] {self.id}'


if __name__ == '__main__': # test 없이 바로 실행 해보는 코드
    h = HousingService()
    ic(h.new_model())


'''
<class 'pandas.core.frame.DataFrame'>
RangeIndex: 20640 entries, 0 to 20639
Data columns (total 10 columns):
 #   Column              Non-Null Count  Dtype
---  ------              --------------  -----
 0   longitude           20640 non-null  float64
 1   latitude            20640 non-null  float64
 2   housing_median_age  20640 non-null  float64
 3   total_rooms         20640 non-null  float64
 4   total_bedrooms      20433 non-null  float64
 5   population          20640 non-null  float64
 6   households          20640 non-null  float64
 7   median_income       20640 non-null  float64
 8   median_house_value  20640 non-null  float64
 9   ocean_proximity     20640 non-null  object
dtypes: float64(9), object(1)
memory usage: 1.6+ MB

'''