from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.tensor.models import Calculator, FashionClassification, TensorFunction


@api_view(['GET'])
@parser_classes([JSONParser])
def calculator(request):
    Calculator().process()
    return JsonResponse({'result': ' Calculator Process SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def fashionClassification(request):
    FashionClassification().process()
    return JsonResponse({'result': ' FashionClassification Process SUCCESS'})

@api_view(['GET'])
@parser_classes([JSONParser])
def fashionClassification_Fashion(request):
    FashionClassification().fashion()
    return JsonResponse({'result': ' FashionClassification Fashion SUCCESS'})


@api_view(['GET'])
@parser_classes([JSONParser])
def tensorFunction(request):
    TensorFunction().hook()
    return JsonResponse({'result': ' TensorFunction Tf_Function SUCCESS'})