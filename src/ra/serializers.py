from rest_framework import serializers
from ra import models

class RaCategorySerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RaCategory
		

class RaDistrictSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RaDistrict
		
		
class RaMainSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RaMain

class RaParameterSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RaParameter

class RaSubParameterSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RaSubParameter

class RaTalukSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RaTaluk

class RaYearSerializer(serializers.ModelSerializer):
	class Meta:
		model = models.RaYear
		

		
	
	
	
