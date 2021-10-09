import re

import pandas as pd
# from django.db import models

# Create your models here.
from icecream import ic
# from matplotlib import pyplot as plt

from admin.common.models import ValueObject, Reader, Printer


# cctv의 배분을 가능 효율적으로 해라 (범죄률 발생 건과 현재 설치되어 있는 현황에 근거하여 작성)
class CrimeCctvModel(object):

    dfg = ValueObject()
    dfr = Reader()
    dfp = Printer()

    def __init__(self):
        '''
        Raw Data's features
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''
        self.crime_columns = ['살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생']  # Nominal
        self.arrest_columns = ['살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']  # Nominal
        self.arrest_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']  # Ratio
        self.cctv_columns = ['기관명', '소계', '2013년도이전', '2014년', '2015년', '2016년']

    def create_crime_model(self) -> object:
        generator = self.dfg
        reader = self.dfr
        printer = self.dfp
        generator.context = 'admin/crime_seoul/data/'
        generator.fname = 'crime_in_Seoul'  #, 'population_in_Seoul.xls', 'CCTV_in_Seoul.csv'
        crime_file_name = reader.new_file(generator)
        print(f'*'*30)
        print(f'파일명: {crime_file_name}')
        print(f'*' * 30)
        crime_model = reader.csv(crime_file_name)
        printer.dframe(crime_model)
        return crime_model

    '''
    <class 'pandas.core.frame.DataFrame'>
    RangeIndex: 31 entries, 0 to 30
    Data columns (total 11 columns):
     #   Column  Non-Null Count  Dtype
    ---  ------  --------------  -----
     0   관서명     31 non-null     object
     1   살인 발생   31 non-null     int64
     2   살인 검거   31 non-null     int64
     3   강도 발생   31 non-null     int64
     4   강도 검거   31 non-null     int64
     5   강간 발생   31 non-null     int64
     6   강간 검거   31 non-null     int64
     7   절도 발생   31 non-null     int64
     8   절도 검거   31 non-null     int64
     9   폭력 발생   31 non-null     int64
     10  폭력 검거   31 non-null     int64
    dtypes: int64(10), object(1)
    '''

    def create_police_position(self) -> object:
        crime = self.create_crime_model() # 위의 메소드 함수 호출 / 'self' 나의 메소드에서 인스턴스 호출
        reader = self.dfr
        station_names = []
        # for name in crime['관서명'] :
        #     station_names.append('서울'+ str(name[:-1]+'경찰서'))
        [station_names.append('서울' + str(name[:-1]+'경찰서')) for name in crime['관서명']]
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
            print(f' {name} : {temp[0].get("formatted_address")}')
        gu_names = []
        for name in station_addrs:
            temp = name.split()
            gu_name = [gu for gu in temp if gu[-1] == '구'][0]
            gu_names.append(gu_name)
        crime['구별'] = gu_names  # '구별'이라는 '열' 자동 생성 (존재하지 않기 때문)/ 이미 있을 경우 덮어 쓰기
        # crime['위도'] = station_lats
        # crime['경도'] = station_lngs
        # 구와 경찰서의 위치가 다른 경우 수작업 / 구글에서 바로 가져오기에
        # crime.loc[crime['관서명'] == '혜화서', ['구별']] == '종로구'  # 비교 구분
        # crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'  # 값 삽입 및 변경
        # crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        # crime.loc[crime['관서명'] == '강서서', ['구별']] = '양천구'
        # crime.loc[crime['관서명'] == '종암서', ['구별']] = '성북구'
        # crime.loc[crime['관서명'] == '방배서', ['구별']] = '서초구'
        # crime.loc[crime['관서명'] == '수서서', ['구별']] = '강남구'
        print(f"샘플 정보 확인 : {crime[crime['관서명'] == '혜화서']}")
        print(f"샘플 정보 확인 : {crime[crime['관서명'] == '금천서']}")
        # crime, loc, crime['관서명'] : dataframe
        crime.to_csv(self.dfg.context+'new_data/police_position(2).csv', index=False)  # 주소(변형된, new-model) 한번 저장 후, 주석 처리
        return crime

    def create_crime_sum(self):
        # # crime_sum = self.create_police_position()
        # # cctv = self.create_cctv_model()
        # crime = self.dfr.csv('admin/crime_seoul/data/new_data/police_position')
        # cctv = self.dfr.csv('admin/crime_seoul/data/new_data/cctv_model')
        # crime_sum_1 = crime.loc[:, ['구별']]
        # # crime_sum_1 = crime_sum['구별']
        # # crime_sum_1['총 범죄 수'] = crime.loc[:, crime.columns != re.compile('검거$')].sum(axis=1)
        # # crime_sum_1_1 = crime_sum[crime_sum[:] == re.compile('발생$')]
        # # crime_sum_1_1 = crime_sum.loc[:, [crime_sum.columns == re.compile('발생$')]]
        # # crime_sum_1['총 범죄 수'] = crime_sum_1_1.sum(axis=1)
        # crime_sum_1['총 범죄 수'] = crime.loc[:, self.crime_columns].sum(axis=1)
        # crime_sum_1['총 검거 수'] = crime.loc[:, self.arrest_columns].sum(axis=1)
        # # crime_sum_1['총 범죄 수'], ['총 검거 수'] = crime_sum.loc[:, self.crime_columns].sum(axis=1), crime_sum.loc[:, self.arrest_columns].sum(axis=1)
        # crime_sum_2 = crime_sum_1.groupby('구별').sum()
        # crime_sum_2['총 검거율'] = crime_sum_2['총 검거 수'] / crime_sum_2['총 범죄 수'] * 100
        # join = pd.merge(cctv.loc[:, ['구별', '소계']], crime_sum_2, on='구별')
        # print('*' * 100)
        # print(join)
        # print('*' * 100)


        # crime = self.dfr.csv('admin/crime_seoul/data/new_data/police_position').groupby('구별').sum()
        # # cctv = self.dfr.csv('admin/crime_seoul/data/new_data/cctv_model')
        # # crime_sum_1 = crime.groupby('구별').sum()
        # # crime_sum = {}
        # crime_sum_1 = crime.loc[crime.columns != re.compile(' 검거$')]
        # print(crime_sum_1)
        # # crime_sum_2 = crime.loc[:, [crime.columns != re.compile('범죄$')]]
        # # crime_sum['총 범죄 수'] = crime_sum_1.sum(axis=1)
        # # crime_sum['총 검거 수'] = crime_sum_2.sum(axis=1)
        # #
        # # print(crime_sum)
        # # crime_sum['구별'] = crime.loc[:, ['구별']]
        # # join = pd.merge(cctv.loc[:, ['구별', '소계']], crime_sum, on='구별')
        # # print('*' * 100)
        # # print(join)
        # # print('*' * 100)

        crime = pd.read_csv('admin/crime_seoul/data/new_data/police_position(2).csv').groupby('구별').sum()
        cctv = pd.read_csv('admin/crime_seoul/data/new_data/cctv_model.csv')
        # p = crime.columns
        # print(crime)
        # c = crime.loc[:, ['Unnamed: 0']]
        # a = re.compile(' 발생$')
        # c = p.str.contains(' 검거$', case=False, regex=True)
        # a = p.str.contains(' 발생$', case=False, regex=True)
        # c = crime[2].str.contains('구', case=False, regex=True)
        crime['총 범죄 수'] = crime.loc[:, crime.columns.str.contains(' 발생$', case=False, regex=True)].sum(axis=1)
        crime['총 검거 수'] = crime.loc[:, crime.columns.str.contains(' 검거$', case=False, regex=True)].sum(axis=1)
        # crime['총 검거 수'] = crime.loc[:, c].sum(axis=1)
        crime['총 검거율'] = crime['총 검거 수'] / crime['총 범죄 수'] * 100
        print(crime)
        join = pd.merge(cctv.loc[:, ['구별', '소계']], crime.loc[:, '총 범죄 수':'총 검거율'], on='구별')
        print(join)

        # # generator = self.dfg
        # # reader = self.dfr
        # # generator.context = 'admin/crime_seoul/data/new_data/'
        # # generator.fname = 'police_position'  # , 'population_in_Seoul.xls', 'CCTV_in_Seoul.csv'
        # # new_crime_file_name = reader.new_file(generator)
        # # crime_sum_1 = reader.csv_header_use(new_crime_file_name, 0, ['구별', '살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생'])
        # # crime_sum_2 = reader.csv_header_use(new_crime_file_name, 0, ['구별', '살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거'])
        # crime_sum = self.create_police_position()
        # cctv = self.create_cctv_model()
        # crime_sum_1 = crime_sum.loc[crime_sum.columns == re.compile('발생$')]
        # # crime_sum_1 = crime_sum.loc[:, ['구별', '살인 발생', '강도 발생', '강간 발생', '절도 발생', '폭력 발생']]
        # crime_sum_2 = crime_sum.loc[:, ['구별', '살인 검거', '강도 검거', '강간 검거', '절도 검거', '폭력 검거']]
        # crime_sum_1['총 범죄 수'] = crime_sum_1.sum(axis=1)
        # crime_sum_1['총 검거 수'] = crime_sum_2.sum(axis=1)
        # # crime_sum_1['총 검거율'] = crime_sum_1['총 검거 수']/crime_sum_1['총 범죄 수'] * 100
        # crime_sum_3 = crime_sum_1.loc[:,['구별', '총 범죄 수', '총 검거 수']]
        # # last = join.loc[:, ['구별', '소계', '총 범죄 수', '총 검거 수', '총 검거율']]
        # # last = join.groupby('구별', as_index=False).mean()
        # last = crime_sum_3.groupby('구별').sum()
        # last['총 검거율'] = last['총 검거 수']/last['총 범죄 수'] * 100
        # last1 = cctv.loc[:, ['구별', '소계']]
        # join = pd.merge(last1, last, on='구별')
        # # print(crime_sum_1)
        # join.to_csv('admin/crime_seoul/data/new_data/crime_sum(test_5).csv')
        # # print(f'!!!!!!!!!!!!!!!!!!test!!!!!!!!!!!!!!!!!!!!!{last1}')
        # print('*'*100)
        # print(join)
        # print('*' * 100)
        # # ic(last.corr())

        '''
                 총 검거 수   총 범죄 수  총 검거율    소계
        총 검거 수  1.000000  0.980313 -0.120028 -0.155695
        총 범죄 수  0.980313  1.000000 -0.306195 -0.178552
        총 검거율  -0.120028 -0.306195  1.000000  0.100789
        소계     -0.155695 -0.178552  0.100789  1.000000

        '''



    def create_cctv_model(self):
        generator = self.dfg
        reader = self.dfr
        printer = self.dfp
        generator.context = 'admin/crime_seoul/data/'
        generator.fname = 'CCTV_in_Seoul'  # , 'population_in_Seoul.xls', 'CCTV_in_Seoul.csv'
        cctv_file_name = reader.new_file(generator)
        print(f'*' * 30)
        print(f'파일명: {cctv_file_name}')
        print(f'*' * 30)
        cctv_model = reader.csv(cctv_file_name)
        printer.dframe(cctv_model)
        cctv_model.rename(columns={'기관명': '구별'}, inplace=True)
        # cctv_model.rename(columns={cctv_model.columns[0]:'구별'}, inplace=True)
        # columns 은 list, dict 형태 받는데, list는 전 count[]? index[]?// dict 1:1 매칭
        # columns[0]:'구별' = key : val ㅁ
        # cctv_model['기관명'] = cctv_model['구별']

        # cctv_model.to_csv(self.dfg.context+'new_data/cctv_model.csv')
        return cctv_model

    def jion_crime_cctv_model(self):
        d1 = self.create_police_position()
        d2 = self.create_cctv_model()
        # d1 = pd.read_csv('../new_data/cctv_model.csv', delimiter=',')
        # d2 = pd.read_csv('../new_data/police_position.csv', delimiter=',')
        join = pd.merge(d1, d2, on='구별')
        join.to_csv(self.dfg.context+'new_data/join_crime_cctv_model.csv')
        print(join)

    def jion_cctv_population_model(self):
        d1 = self.create_population_model()
        d2 = self.create_cctv_model()
        # self.dfg.context = 'admin/crime_seoul/data/'
        # d1 = pd.read_csv('admin/crime_seoul/data/new_data/cctv_model.csv', delimiter=',')
        # d2 = pd.read_csv('admin/crime_seoul/data/new_data/population_model.csv', delimiter=',')
        merge = pd.merge(d1, d2, on='구별')
        '''
        r이 -1.0과 -0.7 사이이면, 강한 음적 선형관계, #
        r이 -0.7과 -0.3 사이이면, 뚜렷한 음적 선형관계,
        r이 -0.3과 -0.1 사이이면, 약한 음적 선형관계,
        r이 -0.1과 +0.1 사이이면, 거의 무시될 수 있는 선형관계,
        r이 +0.1과 +0.3 사이이면, 약한 양적 선형관계,
        r이 +0.3과 +0.7 사이이면, 뚜렷한 양적 선형관계,
        r이 +0.7과 +1.0 사이이면, 강한 양적 선형관계
        '''
        ic(merge.corr())
        '''
        ic| merge.corr():                인구수   한국인    외국인      고령자     CCTV 소계  2013년도이전  2014년     2015년     2016년
                          인구수        1.000000  0.998061 -0.153371  0.932667  [0.306342]   0.168177  0.027040  0.368912  0.144959
                          한국인        0.998061  1.000000 -0.214576  0.931636  [0.304287]   0.163142  0.025005  0.363796  0.145966
                          외국인       -0.153371 -0.214576  1.000000 -0.155381 [-0.023786]   0.048973  0.027325  0.013301 -0.042688
                          고령자        0.932667  0.931636 -0.155381  1.000000  [0.255196]   0.105379  0.010233  0.372789  0.065784
                          소계         0.306342  0.304287 -0.023786  0.255196   1.000000   0.862756  0.450062  0.624402  0.593398
                          2013년도 이전  0.168177  0.163142  0.048973  0.105379  0.862756   1.000000  0.121888  0.257748  0.355482
                          2014년      0.027040  0.025005  0.027325  0.010233  0.450062   0.121888  1.000000  0.312842  0.415387
                          2015년      0.368912  0.363796  0.013301  0.372789  0.624402   0.257748  0.312842  1.000000  0.513767
                          2016년      0.144959  0.145966 -0.042688  0.065784  0.593398   0.355482  0.415387  0.513767  1.000000
                          
                          # cctv의 총 갯수를 기준으로 인구수와의 관계 확인
                          # → 과거, 인구 수에 대비하여 CCTV 배분 / 한국인의 수와 연관관계 있지만, 외국인과의 관계 없음.
        '''
        # merge.to_csv(self.dfg.context+'new_data/jion_cctv_population_model.csv')
        # print(merge)

    def create_population_model(self) -> object:
        generator = self.dfg
        reader = self.dfr
        printer = self.dfp
        generator.context = 'admin/crime_seoul/data/'
        generator.fname = 'population_in_Seoul'  # , 'population_in_Seoul.xls', 'CCTV_in_Seoul.csv'
        population_file_name = reader.new_file(generator)
        print(f'*' * 30)
        print(f'파일명: {population_file_name}')
        print(f'*' * 30)
        population_model = reader.xls(population_file_name, 2, ('B, D, G, J, N'))
        # population_model.rename(columns={'자치구': '구별',  # 값 찾아서 변경하기
        #                                  '합계': '인구수',
        #                                  '한국인': '한국인',
        #                                  '등록외국인': '외국인',
        #                                  '65세이상고령자': '고령자'},
        #                         inplace=True)
        # population_model.rename(columns={population_model.columns[i]: list[i] for i in range(len(list))}, inplace=True)  # for문으로 순서 대로 일부 변경
        population_model.rename(columns={population_model.columns[0]: '구별',  # index로 변경하기
                                         population_model.columns[1]: '인구수',
                                         population_model.columns[2]: '한국인',
                                         population_model.columns[3]: '외국인',
                                         population_model.columns[4]: '고령자'},
                                inplace=True)
        # ls = ['구별', '인구수', '한국인', '외국인', '고령자']
        # population_model.rename(columns=population_model.columns[i] for i in ls )
        # population_model.columns=['구별', '인구수', '한국인', '외국인', '고령자']  # columns을 전체 열로 변경하기 / 전체이기에 반드시 전체 갯수 맞춰야 함.
        # population_model.rename(columns={'구별', '인구수', '한국인', '외국인', '고령자'}, inplace=True)
        population_model.drop([26], inplace=True)
        printer.dframe(population_model)
        # population_model.to_csv(self.dfg.context + 'new_data/population_model.csv')
        return population_model



# class CrimeSeoul(models.Model): # DB에 저장할 의사 없음 → 필요 없음
#
#     id = models.AutoField(primary_key=True)
#
#     class Meta:
#         db_table = "Crime_Seoul"
#
#         def __str__(self):
#             return f'[{self.pk}] {self.id}'

if __name__ == '__main__':  # test 없이 바로 실행 해보는 코드
    h = CrimeCctvModel()
    ic(h.new_model())
