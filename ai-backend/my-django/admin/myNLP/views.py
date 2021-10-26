from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser


# Create your views here.
from admin.myNLP.models import NaverMovie


@api_view(['GET'])
@parser_classes([JSONParser])
def imdb_process(request):
    return JsonResponse({'Imdb().imdb_process()': 'SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def naver_process(request):
    NaverMovie().naver_process()
    return JsonResponse({'NaverMovie().model_fit()': 'SUCCESS'})