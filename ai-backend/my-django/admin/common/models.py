from django.db import models

# Create your models here.

import pandas as pd
from dataclasses import dataclass
from icecream import ic


@dataclass
class DFrameGenerator(object):
    # context: str
    # fname: str
    train: object
    test: object
    id: str
    label: str
    fname: str

    @property
    def fname(self) -> object: return self._fname

    @fname.setter
    def fname(self, fname): self._fname = fname

    # def dframe(self, fname): self._dframe = pd.read_csv(fname)
    # fname 이 들어오면 자동 pd.read_csv 데이터 프래임으로 변환 //불가

    # @property
    # def context(self) -> str: return self._context
    #
    # @context.setter
    # def context(self, context): self._context = context
    #
    # @property
    # def fname(self) -> str: return self._fname
    #
    # @fname.setter
    # def fname(self, fname): self._fname = fname

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