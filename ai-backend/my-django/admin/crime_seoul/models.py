from django.db import models

# Create your models here.
from icecream import ic
from matplotlib import pyplot as plt

from admin.common.models import DFrameGenerator, Reader, Printer


# cctv의 배분을 가능 효율적으로 해라 (범죄률 발생 건과 현재 설치되어 있는 현황에 근거하여 작성)
class CrimeCctvModel():

    dfg = DFrameGenerator()
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
        crime = self.create_crime_model()
        reader = self.dfr
        station_names = []
        for name in crime ['관서명'] :
            station_names.append('서울'+ str(name[:-1]+'경찰서'))
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
        crime['구별'] = gu_names
        # 구와 경찰서의 위치가 다른 경우 수작업
        crime.loc[crime['관서명'] == '혜화서', ['구별']] = '종로구'
        crime.loc[crime['관서명'] == '서부서', ['구별']] = '은평구'
        crime.loc[crime['관서명'] == '강서서', ['구별']] = '양천구'
        crime.loc[crime['관서명'] == '종암서', ['구별']] = '성북구'
        crime.loc[crime['관서명'] == '방배서', ['구별']] = '서초구'
        crime.loc[crime['관서명'] == '수서서', ['구별']] = '강남구'
        # crime, loc, crime['관서명'] : df
        crime.to_csv(self.dfg.context+'new_data/police_position.csv')




class CrimeSeoulService(object):

    def __init__(self):
        self.dfg = DFrameGenerator()
        self.dfg.fname = 'admin/crime_seoul/data/CCTV_in_Seoul.csv'
        self.model = self.dfg.create_model()

    # def make_df(self):
    #     name = ''
    #     test1 = None
    #     test2 = None
    #     test3 = []
    #     result = None
    #     ls =
    #         ['강남구', '강동구', '강북구', '강서구', '관악구', '광진구', '구로구', '금천구', '노원구', '도봉구', '동대문구', '동작구',
    #           '마포구', '서대문구', '서초구', '성동구', '성북구', '송파구', '양천구', '영등포구', '용산구', '은평구', '종로구', '중구', '중랑구']

    def crime_info(self):
        self.dfg.model_info(self.model)

    def crime_hist(self)-> object:
        self.model.hist(bins=50, figsize=(20, 15))
        plt.savefig('admin/crime_seoul/image/crime_hist.png')

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
    h = CrimeSeoulService()
    ic(h.new_model())
