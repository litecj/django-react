from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.crime_seoul.models import CrimeCctvModel


@api_view(['GET'])
@parser_classes([JSONParser])
def create_crime_model(request):
    CrimeCctvModel().create_crime_model()
    return JsonResponse({'result': 'Create Crime Model SUCCESS'})

def crime_info(request):
    CrimeCctvModel()
    return JsonResponse({'result': 'Crime Info SUCCESS'})

def crime_hist(request):
    return JsonResponse({'result': 'Crime Hist SUCCESS'})


def create_police_position(request):
    CrimeCctvModel().create_police_position()
    return JsonResponse({'result': 'Create Police Position SUCCESS'})

def create_cctv_model(request):
    CrimeCctvModel().create_cctv_model()
    return JsonResponse({'result': 'Create Cctv Model SUCCESS'})

def create_population_model(request):
    CrimeCctvModel().create_population_model()
    return JsonResponse({'result': 'Create Population Model SUCCESS'})