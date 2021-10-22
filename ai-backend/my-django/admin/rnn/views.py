from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser


# Create your views here.
from admin.rnn.models import MyRNN


@api_view(['GET'])
@parser_classes([JSONParser])
def ram_price(request):
    MyRNN().ram_price()
    return JsonResponse({'MyRNN().ram_price()': 'SUCCESS'})