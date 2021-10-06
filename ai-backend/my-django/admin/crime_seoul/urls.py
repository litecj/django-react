from django.conf.urls import url

from admin.crime_seoul import views

urlpatterns = {
    url(r'create-crime-model', views.create_crime_model),
    url(r'create-police-position', views.create_police_position)
}