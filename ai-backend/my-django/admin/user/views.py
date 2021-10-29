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
        ic('======= 회원 목록 진입 ======= ')
        all_users = Member.objects.all()
        ic(all_users)
        serializer = UserSerializer(all_users, many=True)
        ic(serializer.data)
        return JsonResponse(data=serializer.data, safe=False)
    elif request.method == 'POST':
        ic('======= 회원가입 진입 ======= ')
        new_user = request.data
        ic(new_user)
        serializer = UserSerializer(data = new_user)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({'result' : f'Welcome, {serializer.data.get("name")}'}, status=201)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PUT':
        ic('======= 회원 정보 수정 진입 ======= ')
        # new_user = request.data
        # ic(new_user)
        # serializer = UserSerializer(data = new_user)
        # if serializer.is_valid():
        #     serializer.save()
        #     return JsonResponse({'result' : f'Welcome, {serializer.data.get("name")}'}, status=201)
        return None

@api_view(['DELETE', 'GET'])
def check(request, username):         # 파라미터(매개변수)의 조건 값이 다르기에 오보로딩 하여 사용 가능 ??? 확인 必
    if request.method == 'GET':
        ic('======= 회원 개인 정보 진입 ======= ')
        ic(username)
        detailUser = request.data
        ic(detailUser)
        dbUser = Member.objects.get(pk=detailUser['username'])
        print(f'{type(dbUser)}')  # <class 'admin.user.models.User'>
        ic(dbUser)
        userSerializer = UserSerializer(dbUser, many=False)
        return JsonResponse(data=userSerializer.data, safe=False)
    elif request.method == 'DELETE':
        ic('======= 회원 정보 삭제 진입 ======= ')


@api_view(['POST'])
@parser_classes([JSONParser])
def login(request):
    try:
        ic('======= 회원 로그인 진입 ======= ')
        loginUser = request.data
        # print(f'{type(loginUser)}') # <class 'dict'>
        ic(loginUser)
        # serializer = UserSerializer(request.data, many=True)  # serializer : string 값  - 직렬화
        dbUser = Member.objects.get(pk=loginUser['username'])
        ic(dbUser)
        if loginUser['password'] == dbUser.password:
            ic('로그인 성공')
            userSerializer = UserSerializer(dbUser, many=False)
            ic(userSerializer)
            return JsonResponse(data=userSerializer.data, safe=False)
        else:
            print('비밀번호 오류')
            return JsonResponse(data={'result':'PASSWORD-FAIL'}, safe=False)

    except Member.DoesNotExist:
        print('에러발생')
        return JsonResponse(data={'result':'USERNAME-FAIL'}, safe=False)

