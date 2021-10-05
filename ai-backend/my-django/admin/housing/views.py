import matplotlib.pyplot as plt
from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.shortcuts import render
from icecream import ic
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.views import APIView

# Create your views here.
from admin.housing.models import HousingService


@api_view(['GET'])
@parser_classes([JSONParser])
def housing_info(request):
    HousingService().housing_info()
    # h = HousingService()  # 반복적인 활동으로 'common'으로 옮겨 활용
    # hi = h.new_model()
    # ic(hi.head(3))
    # ic(hi.tail(3))
    # ic(hi.info())
    # ic(hi.describe())
    # hi.hist(bins=50, figsize=(20, 15))
    # plt.savefig('admin/housing/image/housing-hist.png')
    return JsonResponse({'result': 'Housing Info SUCCESS'})

def housing_hist(request):
    HousingService().housing_hist()
    return JsonResponse({'result': 'Housing Hist SUCCESS'})

def split_model(request):
    HousingService().split_model()
    return JsonResponse({'result': 'Housing Split Success'})

def income_cat_hist(request):
    h = HousingService()
    h.income_cat_hist()
    return JsonResponse({'result': 'income_cat_hist Save SUCCESS'})

def split_model_by_income_cat(request):
    h = HousingService()
    h.split_model_by_income_cat()
    return JsonResponse({'result': 'income_cat_hist Save SUCCESS'})