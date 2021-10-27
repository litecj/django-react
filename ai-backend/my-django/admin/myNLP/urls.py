from django.conf.urls import url

from admin.myNLP import views

urlpatterns = {
    url(r'homonym_process', views.homonym_process),
    url(r'naver_process', views.naver_process),
}