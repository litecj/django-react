from django.http import JsonResponse
from icecream import ic
from rest_framework import status
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser

from admin.user.models import Member
from admin.user.serializers import UserSerializer



@api_view(['GET', 'POST', 'PUT'])
@parser_classes([JSONParser])
def users(request):
    if request.method == 'GET':
        ic('=====회원 목록 진입 ======= ')
        all_users = Member.objects.all()
        serializer = UserSerializer(all_users, many=True)
        return JsonResponse(data=serializer, safe=False)
    elif request.method == 'POST':
        ic('=====회원가입 진입 ======= ')
        new_user = request.data
        ic(new_user)
        serializer = UserSerializer(data = new_user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result' : f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        ic('=====회원 정보 수정 진입 ======= ')
        # new_user = request.data
        # ic(new_user)
        # serializer = UserSerializer(data = new_user)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse({'result' : f'Welcome, {serializer.data.get("name")}'}, status=201)
        return None

@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def users(request, id):         # 파라미터(매개변수)의 조건 값이 다르기에 오보로딩 하여 사용 가능
    if request.method == 'GET':
        ic('=====회원 개인 정보 진입 ======= ')
    elif request.method == 'POST':
        ic('=====회원 정보 수정 진입 ======= ')

@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    pass

