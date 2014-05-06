from rest_framework import serializers
from ra.models.models import *


class RaSubParameterSerializer(serializers.ModelSerializer):

    class Meta:
        model = RaSubParameter


class RaParameterSerializer(serializers.ModelSerializer):
    subparameters = RaSubParameterSerializer(many=True)

    class Meta:
        model = RaParameter
        fields = ('id', 'name', 'subparameters')


class RaCategorySerializer(serializers.ModelSerializer):
    parameters = RaParameterSerializer(many=True)

    class Meta:
        model = RaCategory
        fields = ('id', 'name', 'parameters')


class RaTalukSerializer(serializers.ModelSerializer):

    class Meta:
        model = RaTaluk


class RaDistrictSerializer(serializers.ModelSerializer):
    taluks = RaTalukSerializer(many=True)

    class Meta:
        model = RaDistrict
        fields = ('id', 'name', 'taluks')


class RaMainSerializer(serializers.ModelSerializer):

    class Meta:
        model = RaMain


class RaYearSerializer(serializers.ModelSerializer):

    class Meta:
        model = RaYear
