import pandas as pd
from django.db import models

# Create your models here.
from icecream import ic
from matplotlib import pyplot as plt

from admin.common.models import ValueObject, Reader, Printer


# cctv의 배분을 가능 효율적으로 해라 (범죄률 발생 건과 현재 설치되어 있는 현황에 근거하여 작성)
class CrimeCctvModel():

    dfg = ValueObject()
    dfr = Reader()
    dfp = Printer()

    def __init__(self):
        '''
        Raw Data's features
        살인 발생,살인 검거,강도 발생,강도 검거,강간 발생,강간 검거,절도 발생,절도 검거,폭력 발생,폭력 검거
        '''
        self.crime_columns = ['살인발생', '강도발생', '강간발생', '절도발생', '폭력발생']  # Nominal
        self.arrest_columns = ['살인검거', '강도검거', '강간검거', '절도검거', '폭력검거']  # Nominal
        self.arrest_rate_columns = ['살인검거율', '강도검거율', '강간검거율', '절도검거율', '폭력검거율']  # Ratio
        self.cctv_columns = ['기관명', '소계', '2013년도이전', '2014년', '2015년', '2016년']

    def create_crime_model(self):
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

    def create_police_position(self):
        crime = self.create_crime_model() # 위의 메소드 함수 호출 / 'self' 나의 메소드에서 인스턴스 호출
        reader = self.dfr
        station_names = []
        # for name in crime['관서명'] :
        #     station_names.append('서울'+ str(name[:-1]+'경찰서'))
        [station_names.append('서울'+ str(name[:-1]+'경찰서')) for name in crime['관서명']]
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
        crime['구별'] = gu_names # '구별'이라는 '열' 자동 생성 (존재하지 않기 때문)/ 이미 있을 경우 덮어 쓰기
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
        # crime.to_csv(self.dfg.context+'new_data/police_position(1).csv')  # 주소(변형된, new-model) 한번 저장 후, 주석 처리
        return crime

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
        cctv_model.rename(columns={'기관명':'구별'}, inplace=True)
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


    def create_population_model(self):
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
        printer.dframe(population_model)
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
