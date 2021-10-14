from django.conf.urls import url

from admin.crime_seoul import views

urlpatterns = {
    url(r'create-crime-model', views.create_crime_model),
    url(r'create-police-position', views.create_police_position),
    url(r'create-cctv-model', views.create_cctv_model),
    url(r'create-population-model', views.create_population_model),
    url(r'jion-crime-cctv-model', views.jion_crime_cctv_model),
    url(r'jion-cctv-population-model', views.jion_cctv_population_model),
    url(r'create-crime-sum', views.create_crime_sum),
    url(r'sum-population-model', views.sum_population_model),




    url(r'process', views.process)
}