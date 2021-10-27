from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

# Create your views here.



@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    return JsonResponse({'process()': 'SUCCESS'})