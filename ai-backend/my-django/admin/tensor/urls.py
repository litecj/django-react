from django.conf.urls import url

from admin.tensor import views

urlpatterns = {
    url(r'calculator', views.calculator),
    url(r'fashion/process', views.fashionClassification),
    url(r'fashion', views.fashionClassification_Fashion),

}