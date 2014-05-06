from rest_framework.response import Response
from rest_framework.decorators import api_view
from ra.serializers.serializers import *
from ra.models.models import *
import MySQLdb
import collections

@api_view(['GET'])
def categories(request):
    category_objects = RaCategory.objects.all().order_by('id')
    return Response(RaCategorySerializer(category_objects).data)

@api_view(['GET'])
def category(request, category_id):
    category_object = RaCategory.objects.get(id=category_id)
    return Response(RaCategorySerializer(category_object).data)

@api_view(['GET'])
def parameters(request):
    parameter_objects = RaParameter.objects.all().order_by('id')
    return Response(RaParameterSerializer(parameter_objects).data)

@api_view(['GET'])
def parameter(request, parameter_id):
    parameter_object = RaParameter.objects.get(id=parameter_id)
    return Response(RaParameterSerializer(parameter_object).data)

@api_view(['GET'])
def subparameters(request):
    subparameter_objects = RaSubParameter.objects.all().order_by('id')
    return Response(RaSubParameterSerializer(subparameter_objects).data)

@api_view(['GET'])
def subparameter(request, subparameter_id):
    subparameter_object = RaSubParameter.objects.get(id=subparameter_id)
    return Response(RaSubParameterSerializer(subparameter_object).data)

@api_view(['GET'])
def years(request):
    years_objects = RaYear.objects.all().order_by('id')
    return Response(RaYearSerializer(years_objects).data)

@api_view(['GET'])
def year(request, year_id):
    year_object = RaYear.objects.get(id=year_id)
    return Response(RaYearSerializer(year_object).data)

@api_view(['GET'])
def taluks(request):
    taluk_objects = RaTaluk.objects.all().order_by('id')
    return Response(RaTalukSerializer(taluk_objects).data)

@api_view(['GET'])
def taluk(request, taluk_id):
    taluk_object = RaTaluk.objects.get(id=taluk_id)
    return Response(RaTalukSerializer(taluk_object).data)

@api_view(['GET'])
def districts(request):
    district_objects = RaDistrict.objects.all().order_by('id')
    return Response(RaDistrictSerializer(district_objects).data)

@api_view(['GET'])
def district(request, district_id):
    district_object = RaDistrict.objects.get(id=district_id)
    return Response(RaDistrictSerializer(district_object).data)

@api_view(['GET'])
def values(request):
    value_objects = RaMain.objects.all().order_by('id')
    return Response(RaMainSerializer(value_objects).data)

@api_view(['GET'])
def value(request, value_id):
    value_object = RaMain.objects.get(id=value_id)
    return Response(RaMainSerializer(value_object).data)

# @api_view(['GET'])
# def template(request):
#     data = {'YearOpts': RaYearSerializer().data, 'CategoryOpts': RaCategorySerializer().data,
#             'ParameterOpts': RaParameterSerializer().data}
#     return Response(data)

