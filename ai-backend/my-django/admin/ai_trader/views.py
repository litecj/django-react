from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser


# Create your views here.
from admin.ai_trader.models import AITrader


@api_view(['GET'])
@parser_classes([JSONParser])
def model_builder(request):
    AITrader().model_builder()
    return JsonResponse({'AITrader().model_builder()': 'SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def process(request):
    AITrader().process()
    return JsonResponse({'AITrader().process()': 'SUCCESS'})
