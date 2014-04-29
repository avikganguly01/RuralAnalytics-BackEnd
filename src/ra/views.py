from rest_framework import viewsets,generics
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from ra.serializers import *
from ra.models import *
import MySQLdb
import collections

class RaCategoryList(generics.ListCreateAPIView):
	model = RaCategory
	serializer_class = RaCategorySerializer

class RaDistrictList(generics.ListCreateAPIView):
	model = RaDistrict
	serializer_class = RaDistrictSerializer

class RaMainList(generics.ListCreateAPIView):
	model = RaMain
	serializer_class = RaMainSerializer
	
class RaParameterList(generics.ListCreateAPIView):
	model = RaParameter
	serializer_class = RaParameterSerializer
	
class RaSubParameterList(generics.ListCreateAPIView):
	model = RaSubParameter
	serializer_class = RaSubParameterSerializer
	
class RaTalukList(generics.ListCreateAPIView):
	model = RaTaluk
	serializer_class = RaTalukSerializer
	
class RaYearList(generics.ListCreateAPIView):
	model = RaYear
	serializer_class = RaYearSerializer


@api_view(['GET'])

def template(request):
    """
    list years, categories and parameters 
    """
    data = { 'YearOpts' : RaYearSerializer().data ,'CategoryOpts' : RaCategorySerializer().data, 'ParameterOpts' : RaParameterSerializer().data }
    return Response(data)

        
@api_view(['GET'])

def subparameters(request,parameter_id):
	sub_parameter_objects= RaSubParameter.objects.filter(parameter=parameter_id)
	return Response(RaSubParameterSerializer(sub_parameter_objects).data,many=True)
