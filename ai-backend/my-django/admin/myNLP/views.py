from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser


# Create your views here.
from admin.myNLP.models import NaverMovie, HomonymClassification


@api_view(['GET'])
@parser_classes([JSONParser])
def homonym_process(request):
    HomonymClassification().process()
    return JsonResponse({'Imdb().homonym_process()': 'SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def naver_process(request):
    NaverMovie().naver_process()
    return JsonResponse({'NaverMovie().model_fit()': 'SUCCESS'})