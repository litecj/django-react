import csv
import re

import folium
import numpy as np
import pandas as pd
# from django.db import models

# Create your models here.
from icecream import ic
# from matplotlib import pyplot as plt
from sklearn import preprocessing

from admin.common.models import ValueObject, Reader, Printer

# cctv의 배분을 가능 효율적으로 해라 (범죄률 발생 건과 현재 설치되어 있는 현황에 근거하여 작성)
class CrimeCctvModel(object):

    def __init__(self):
        pass

    '''
        Raw Data 의 features 를 가져온다
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''

    # noinspection PyMethodMayBeStatic
    def process(self):
        ic('### 프로세스 시작 ###')
        vo = ValueObject()
        reader = Reader()
        printer = Printer()
        vo.context = 'admin/crime_seoul/data/'
        crime_titles = ['살인', '강도', '강간', '절도', '폭력']
        crime_columns = ['살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생']  # Nominal
        arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']  # Nominal
        arrest_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']  # Ratio


        ic('############### [1] CRIME DF CREATION  ###############')
        vo.fname = 'crime_in_Seoul'
        crime_df = reader.csv(reader.new_file(vo))


        ic('############### [2] 경찰서 위치 DF CREATION  ###############')
        # self.crime_police(crime_df, reader, vo) #::: GOOGLE MAP
        vo.fname = 'new_data/crime_police'
        crime_df = reader.csv(reader.new_file(vo))


        ic('############### [3] cctv_df CREATION  CCTV DF CREATION  ###############')
        vo.fname = 'CCTV_in_Seoul'
        cctv_df = reader.csv(reader.new_file(vo))
        cctv_df.rename(columns={cctv_df.columns[0]: '구별'}, inplace=True)


        ic('############### [4] POP DF CREATION  ###############')

        vo.fname = 'population_in_Seoul'
        pop_df = reader.xls(reader.new_file(vo), 2, 'B, D, G, J, N')
        pop_df.columns = ['구별', '인구수', '한국인', '외국인', '고령자']
        pop_df.drop([26], inplace=True)


        ic('############### [5] CCTV_POP DF 생성 ###############')
        cctv_pop_df = pd.merge(cctv_df, pop_df)
        cctv_pop_corr = cctv_pop_df.corr()
        ic(cctv_pop_corr)

        '''
               CCTV와 상관계수: 한국인 0.3, 외국인 0, 고령자 0.2   
        '''

        ic('############### [6] CCTV_CRIME DF CREATION  ###############')
        crime_df = crime_df.groupby('구별').sum()
        crime_df['총 범죄 수'] = crime_df.loc[:, crime_df.columns.str.contains(' 발생$', case=False, regex=True)].sum(axis=1)
        crime_df['총 검거 수'] = crime_df.loc[:, crime_df.columns.str.contains(' 검거$', case=False, regex=True)].sum(axis=1)
        crime_df['총 검거율'] = crime_df['총 검거 수'] / crime_df['총 범죄 수'] * 100
        # cctv_df['총 CCTV'] = cctv_df.loc[cctv_df.columns.str.contains('년*', case=False, regex=True)].sum(axis=1)
        crime_cctv_df = pd.merge(cctv_df.loc[:, ['구별', '소계']], crime_df.loc[:, '총 범죄 수':'총 검거율'], on='구별')
        crime_cctv_df.rename(columns={'소계': 'CCTV 총합'}, inplace=True)
        crime_cctv_df.to_csv('admin/crime_seoul/data/new_data/test(3).csv')
        ic(crime_cctv_df.corr())
        '''
                    ############### CCTV_CRIME DF CREATION  ###############
                      CCTV 총합    총 범죄 수    총 검거 수     총 검거율
            CCTV 총합  1.000000  0.474269  0.520321  0.121538
            총 범죄 수   0.474269  1.000000  0.979473 -0.158565
            총 검거 수   0.520321  0.979473  1.000000  0.036248
            총 검거율    0.121538 -0.158565  0.036248  1.000000
            
            CCTV와 상관계수: 범죄수 0.47, 검거수 0.52 
        '''

        # test
        # print('############### CCTV_CRIME DF 생성 ###############')
        # crime_df['총 범죄 수'] = crime_df.loc[:, crime_columns].sum(axis=1)
        # crime_df['총 검거 수'] = crime_df.loc[:, arrest_columns].sum(axis=1)
        # crime_sum_2 = crime_df.groupby('구별').sum()
        # crime_sum_2['총 검거율'] = crime_sum_2['총 검거 수'] / crime_sum_2['총 범죄 수'] * 100
        # crime_cctv_df = pd.merge(cctv_df.loc[:, ['구별', '소계']], crime_sum_2.loc[:, '총 범죄 수':'총 검거율'], on='구별')
        # print('*' * 100)
        # print(crime_cctv_df.corr())
        # print('*' * 100)

        '''
            ****************************************************************************************************
                          소계    총 범죄 수    총 검거 수     총 검거율
            소계      1.000000  0.474269  0.520321  0.121538
            총 범죄 수  0.474269  1.000000  0.979473 -0.158565
            총 검거 수  0.520321  0.979473  1.000000  0.036248
            총 검거율   0.121538 -0.158565  0.036248  1.000000
            ****************************************************************************************************
        '''



        ic('############### [6]  POLICE DF CREATION  ###############')
        police_df = pd.pivot_table(crime_df, index='구별', aggfunc= np.sum)
        ic(police_df)
        ic(f'경찰서DF 컬럼: {police_df.columns}')
        '''
         ['강간 검거', '강간 발생', '강도 검거', '강도 발생', '살인 검거', '살인 발생','절도 검거', 
         '절도 발생', '총검거수', '총검거율', '총범죄수', '폭력 검거', '폭력 발생']
        '''
        for i, j in enumerate(crime_columns):
            police_df[arrest_rate_columns[i]] = \
                (police_df[arrest_columns[i]].astype(int) / police_df[j].astype(int)) * 100
        # police_df['살인검거율'] = (police_df['살인 검거'].astype(int) / police_df['살인 발생'].astype(int)) * 100
        # police_df['강도검거율'] = (police_df['강도 검거'].astype(int) / police_df['강도 발생'].astype(int)) * 100
        # police_df['강간검거율'] = (police_df['강간 검거'].astype(int) / police_df['강간 발생'].astype(int)) * 100
        # police_df['절도검거율'] = (police_df['절도 검거'].astype(int) / police_df['절도 발생'].astype(int)) * 100
        # police_df['폭력검거율'] = (police_df['폭력 검거'].astype(int) / police_df['폭력 발생'].astype(int)) * 100
        police_df.drop(columns=dict(zip(arrest_columns, [])), axis=1, inplace=True)
        for i in arrest_rate_columns:
            police_df.loc[police_df[i] > 100, 1] = 100  # 데이터값 기간이 1년을 넘긴 경우가 있어서 100을 max 로 지정
        keys = [f'{i} 발생' for i in crime_titles]
        columns = dict(zip(keys, crime_titles))
        police_df.rename(columns=columns, inplace=True)
            # police_df.rename(columns={
            #     '살인 발생': '살인',
            #     '강도 발생': '강도',
            #     '강간 발생': '강간',
            #     '절도 발생': '절도',
            #     '폭력 발생': '폭력'
            # }, inplace=True)
        x = police_df[arrest_rate_columns].values
        # from sklearn import preprocessing 추가
        min_max_scalar = preprocessing.MinMaxScaler()
        # 스케일링은 선형변환을 적용하여 전체 자료의 분포를 평균 0, 분산 1이 되도록 만드는 과정
        x_scaled = min_max_scalar.fit_transform(x.astype(float))
        # 정규화 normalization
        # 1. 빅데이터를 처리하면서 데이터의 범위(도메인)을 일치시킨다
        # 2. 분포(스케일)을 유사하게 만든다

        ic('############### [7]  POLICE NORM DF CREATION  ###############')
        police_norm_df = pd.DataFrame(x_scaled, columns=crime_columns, index=police_df.index)
        police_norm_df[arrest_rate_columns] = police_df[arrest_rate_columns]
        police_norm_df['범죄'] = np.sum(police_norm_df[crime_columns], axis=1)
        police_norm_df['검거'] = np.sum(police_norm_df[arrest_rate_columns], axis=1)
        police_norm_df.to_csv(vo.context + 'new_data/police_norm.csv', sep=',', encoding='UTF-8')
        police_norm_df = pd.read_csv(vo.context + 'new_data/police_norm.csv')
        ic(police_norm_df.columns)
        temp = crime_df[arrest_columns] / crime_df[arrest_columns].max()
        crime_df['검거'] = np.sum(temp, axis=1)
        crime_police_tuple = tuple(zip(police_norm_df['구별'], police_norm_df['범죄']))



        ic('############### [8]  SEOUL MAP CREATION  ###############')
        vo.fname = 'geo_simple'
        state_geo = reader.json(reader.new_file(vo))

        map = folium.Map(location=[37.5502, 126.982], zoom_start=12, title='Stamen Toner')

        folium.Choropleth(
            geo_data=state_geo,
            name="choropleth",
            data=crime_police_tuple,
            columns=["Gu", "Crime Rate"],
            key_on="feature.id",
            fill_color="PuRd",
            fill_opacity=0.7,
            line_opacity=0.2,
            legend_name="Crime Rate (%)",
        ).add_to(map)

        folium.LayerControl().add_to(map)
        for i in crime_df.index:
            folium.CircleMarker([crime_df['lat'][i], crime_df['lng'][i]],
                                radius=crime_df['검거'][i] * 10,
                                fill_color='#0a0a32').add_to(map)

        map.save(vo.context + 'new_data/folium.html')








    def crime_police(self, crime_df, reader, vo):
        station_names = []
        for name in crime_df['관서명']:
            station_names.append('서울' + str(name[:-1] + '경찰서'))
        station_addrs = []
        station_lats = []
        station_lngs = []
        gmaps = reader.gmaps()
        for name in station_names:
            temp = gmaps.geocode(name, language='ko')
            station_addrs.append(temp[0].get('formatted_address'))
            temp_loc = temp[0].get('geometry')
            station_lats.append(temp_loc['location']['lat'])
            station_lngs.append(temp_loc['location']['lng'])
        crime_df['lat'] = station_lats
        crime_df['lng'] = station_lngs
        gu_names = []
        for name in station_addrs:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime_df['구별'] = gu_names
        crime_df.loc[19,'구별'] = '강서구'
        print(crime_df[crime_df['관서명'] == '강서서'])

        crime_df.to_csv(vo.context+'new_data/crime_police.csv')
        dt = dict(zip(station_lats, station_lngs))
        print(dt)
        with open(vo.context+'new_data/with_save.csv', 'w', encoding='UTF-8') as f:
            w = csv.writer(f)
            w.writerow(dt.keys())
            w.writerow(dt.values())

