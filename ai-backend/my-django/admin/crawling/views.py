from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.crawling.models import Crawling, NewsCrawling


@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    Crawling().process()
    return JsonResponse({'result': ' Crawling Process SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def newsProcess(request):
    NewsCrawling()
    return JsonResponse({'result': ' NewsCrawling Process SUCCESS'})
