import json
from abc import abstractmethod, ABCMeta

import googlemaps
from django.db import models
import pandas as pd
from dataclasses import dataclass
from icecream import ic

# Create your models here.


@dataclass
class ValueObject(object):

    context: str
    train: object
    test: object
    id: str
    label: str
    fname: str
    url: str
    dframe: object

    @property
    def fname(self) -> object: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    # def dframe(self, fname): self._dframe = pd.read_csv(fname)
    # fname 이 들어오면 자동 pd.read_csv 데이터 프래임으로 변환 //불가

    @property
    def context(self) -> str: return self._context

    @context.setter
    def context(self, context): self._context = context

    @property
    def dframe(self) -> str: return self._dframe

    @dframe.setter
    def dframe(self, dframe): self._dframe = dframe

    @property
    def url(self) -> str: return self._url

    @url.setter
    def url(self, url): self._url = url

    @property
    def train(self) -> object: return self._train

    @train.setter
    def train(self, train): self._train = train

    @property
    def test(self) -> object: return self._test

    @test.setter
    def test(self, test): self._test = test

    @property
    def id(self) -> str: return self._id

    @id.setter
    def id(self, id): self._id = id

    @property
    def label(self) -> str: return self._label

    @label.setter
    def label(self, label): self._label = label

    def create_model(self):
        return pd.read_csv(self.fname)

    def model_info(self, model):
        ic(model.head(3))
        ic(model.tail(3))
        ic(model.info())
        ic(model.describe())

class ReaderBase(metaclass=ABCMeta):  # @abstractmethod 때문에 추상 메소드 됨.
    @abstractmethod
    def new_file(self):
        pass

    @abstractmethod
    def csv(self):
        pass

    @abstractmethod
    def xls(self):
        pass

    @abstractmethod
    def json(self):
        pass

class PrinterBase(metaclass=ABCMeta):
    @abstractmethod
    def dframe(self):
        pass

class Reader(ReaderBase):
    def new_file(self, file) -> str :
        return file.context + file.fname

    def csv(self, file) -> object:
        return pd.read_csv(f'{file}.csv', encoding='UTF-8', thousands=',')

    def csv_header(self, file, header) -> object:
        return pd.read_csv(f'{file}.csv', encoding='UTF-8', thousands=',', header=header)

    def csv_header_use(self, file, header, usecols) -> object:
        return pd.read_csv(f'{file}.csv', encoding='UTF-8', thousands=',', header=header, usecols=usecols)


    def xls(self, file, header, usecols) -> object:
        return pd.read_excel(f'{file}.xls', header=header , usecols=usecols)

    def json(self, file):
        # return pd.read_json(f'{file}.json', encoding='UTF-8')
        return json.load(open(f'{file}.json', encoding='UTF-8'))

    def gmaps(self) -> object:
        return googlemaps.Client(key='')

class Printer(PrinterBase):
    def dframe(self, this):
        ic(this.head(3))
        ic(this.tail(3))
        print(this.info())
        ic(this.describe())
        # ic(this.columns())
        print(f'!!Null Count is  {this.isnull().sum()}')