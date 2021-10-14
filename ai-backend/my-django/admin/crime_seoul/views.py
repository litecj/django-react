from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.crime_seoul.models import CrimeCctvModel
from admin.crime_seoul.models_old import CrimeCctvModelOld


@api_view(['GET'])
@parser_classes([JSONParser])
def create_crime_model(request):
    CrimeCctvModelOld().create_crime_model()
    return JsonResponse({'result': 'Create Crime Model SUCCESS'})

def crime_info(request):
    CrimeCctvModelOld()
    return JsonResponse({'result': 'Crime Info SUCCESS'})

def crime_hist(request):
    return JsonResponse({'result': 'Crime Hist SUCCESS'})


def create_police_position(request):
    CrimeCctvModelOld().create_police_position()
    return JsonResponse({'result': 'Create Police Position SUCCESS'})

def create_cctv_model(request):
    CrimeCctvModelOld().create_cctv_model()
    return JsonResponse({'result': 'Create Cctv Model SUCCESS'})

def create_population_model(request):
    CrimeCctvModelOld().create_population_model()
    return JsonResponse({'result': 'Create Population Model SUCCESS'})

def jion_crime_cctv_model(request):
    CrimeCctvModelOld().jion_crime_cctv_model()
    return JsonResponse({'result': 'Jion Crime Cctv Model SUCCESS'})

def jion_cctv_population_model(request):
    CrimeCctvModelOld().jion_cctv_population_model()
    return JsonResponse({'result': 'Jion Cctv Population Model SUCCESS'})

def create_crime_sum(request):
    CrimeCctvModelOld().create_crime_sum()
    return JsonResponse({'result': 'Create Crime Sum Model SUCCESS'})

def sum_population_model(request):
    CrimeCctvModelOld().sum_population_model()
    return JsonResponse({'result': 'Sum Population Model SUCCESS'})

def process(request):
    CrimeCctvModel().process()
    return JsonResponse({'result': 'Process SUCCESS'})