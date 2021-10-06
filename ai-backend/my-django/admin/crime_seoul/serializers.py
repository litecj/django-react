from rest_framework import serializers
# pip install Django django-rest-framework
from .models import CrimeCctvModel as crime_seoul

# class CrimeSeoulSerializer(serializers.Serializer):
#
#     id = serializers.CharField()
#
#     class Meta:
#         model = crime_seoul
#         fields = '__all__'
#
#     def create(self, validated_data):
#         return crime_seoul.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         crime_seoul.objects.filter(pk=instance.id).update(**validated_data)