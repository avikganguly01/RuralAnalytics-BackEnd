from rest_framework.response import Response
from django.http import HttpResponse
from rest_framework.decorators import api_view
from ra.serializers.serializers import *
from ra.models.models import *
import logging
import json

logger = logging.getLogger(__name__)

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
    categoryId = request.GET.get('categoryId')
    parameterId = request.GET.get('parameterId')
    subparameterId = request.GET.get('subparameterId')
    talukId = request.GET.get('talukId')
    yearId = request.GET.get('yearId')
    if yearId != '0':
        if talukId != '0':
            if subparameterId != '0':
               logger.error('Hello1')
               value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, s.name as subparameter,'
                                                        't.name as taluk from ra_main v, ra_sub_parameter s,'
                                                        ' ra_taluk t, ra_year y where v.year_id=' + yearId + ' and v.taluk_id='
                                                        + talukId + ' and v.sub_parameter_id=' + subparameterId + ' and '
                                                        'v.year_id=y.id and v.taluk_id=t.id and v.sub_parameter_id=s.id')
            elif subparameterId == '0':
                if parameterId != '0':
                    logger.error('Hello2')
                    value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, p.name as parameter,'
                                                             's.name as subparameter,t.name as taluk from ra_main v,'
                                                             ' ra_sub_parameter s,ra_parameter p, ra_taluk t, ra_year y'
                                                             ' where v.year_id=' + yearId + ' and v.taluk_id=' + talukId + ' and p.id = ' + parameterId + ' and '
                                                             'v.year_id=y.id and v.taluk_id=t.id and v.sub_parameter_id'
                                                             '=s.id and s.parameter_id=p.id')
                elif parameterId == '0':
                    if categoryId != '0':
                        logger.error('Hello3')
                        value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, c.name as category, p.name as parameter,'
                                                                 ' s.name as subparameter, t.name as taluk from ra_main v, ra_sub_parameter s,'
                                                                 'ra_parameter p, ra_category c, ra_taluk t, ra_year y where v.year_id=' + yearId + ' and'
                                                                 ' v.taluk_id=' + talukId + ' and c.id = ' + categoryId + ' and v.year_id=y.id and v.taluk_id=t.id'
                                                                 ' and v.sub_parameter_id=s.id and s.parameter_id=p.id and c.id=p.category_id')
                    elif categoryId == '0':
                        logger.error('Hello4')
                        value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, s.name as subparameter,'
                                                                 't.name as taluk from ra_main v, ra_sub_parameter s,ra_parameter p,'
                                                                 ' ra_category c, ra_taluk t, ra_year y where v.year_id=' + yearId + ' and'
                                                                 ' v.taluk_id=' + talukId + ' and v.year_id=y.id and v.taluk_id=t.id'
                                                                 ' and v.sub_parameter_id=s.id and s.parameter_id=p.id and c.id=p.category_id')
        elif talukId == '0':
            if subparameterId != '0':
                logger.error('Hello5')
                value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, s.name as subparameter,'
                                                         't.name as taluk from ra_main v, ra_sub_parameter s, ra_taluk '
                                                         't, ra_year y where v.year_id=' + yearId + ' and v.sub_parameter_id=' + subparameterId + ' and '
                                                         'v.year_id=y.id and v.taluk_id=t.id and v.sub_parameter_id=s.id')
            elif subparameterId == '0':
                if parameterId != '0':
                    logger.error('Hello6')
                    value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, p.name as parameter,'
                                                             ' s.name as subparameter,t.name as taluk from ra_main v,'
                                                             ' ra_sub_parameter s, ra_parameter p, ra_taluk t, ra_year y'
                                                             ' where v.year_id=' + yearId + ' and p.id=' + parameterId + ' and v.year_id=y.id and'
                                                             ' v.taluk_id=t.id and v.sub_parameter_id=s.id  and s.parameter_id=p.id')
                elif parameterId == '0':
                    if categoryId != '0':
                        logger.error('Hello7')
                        value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, c.name as category,'
                                                                 ' p.name as parameter, s.name as subparameter,t.name as taluk'
                                                                 ' from ra_main v, ra_sub_parameter s, ra_parameter p, ra_category c,'
                                                                 ' ra_taluk t, ra_year y where v.year_id=' + yearId + ' and c.id=' + categoryId + ' and '
                                                                 'v.year_id=y.id and v.taluk_id=t.id and v.sub_parameter_id=s.id'
                                                                 '  and s.parameter_id=p.id and p.category_id=c.id')
                    elif categoryId == '0':
                        logger.error('Hello8')
                        value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, c.name as category, p.name'
                                                                 ' as parameter, s.name as subparameter,t.name as taluk from ra_main'
                                                                 ' v, ra_sub_parameter s, ra_parameter p, ra_category c, ra_taluk t,'
                                                                 ' ra_year y where v.year_id=' + yearId + ' and v.year_id=y.id and v.taluk_id=t.id'
                                                                 ' and v.sub_parameter_id=s.id  and s.parameter_id=p.id and p.category'
                                                                 '_id=c.id')
    elif yearId == '0':
        if talukId != '0':
            if subparameterId != '0':
                logger.error('Hello9')
                value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, s.name as subparameter, t.name as taluk '
                                                         'from ra_main v, ra_sub_parameter s, ra_taluk t, ra_year y where v.taluk_id=' + talukId + ' and'
                                                         ' v.sub_parameter_id = ' + subparameterId + ' and v.year_id=y.id and v.taluk_id=t.id and v.sub_parameter'
                                                         '_id=s.id')
            elif subparameterId == '0':
                if parameterId != '0':
                    logger.error('Hello10')
                    value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, p.name as parameter, s.name as subparameter,t.name as'
                                                             ' taluk from ra_main v, ra_sub_parameter s,ra_parameter p, ra_taluk t, ra_year y '
                                                             'where v.taluk_id=' + talukId + ' and p.id = ' + parameterId + ' and v.year_id=y.id and v.taluk_id=t.id and '
                                                             'v.sub_parameter_id=s.id and s.parameter_id=p.id')
                elif parameterId == '0':
                    if categoryId != '0':
                        logger.error('Hello11')
                        value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, c.name as category, p.name as parameter,'
                                                                 ' s.name as subparameter,t.name as taluk from ra_main v, ra_sub_parameter s,ra_parameter p,'
                                                                 ' ra_category c, ra_taluk t, ra_year y where v.taluk_id=' + talukId + ' and c.id = ' + categoryId + ' and '
                                                                 'v.year_id=y.id and v.taluk_id=t.id and v.sub_parameter_id=s.id and s.parameter_id=p.id '
                                                                 'and c.id=p.category_id')
                    elif categoryId == '0':
                        logger.error('Hello12')
                        value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year,  c.name as category, p.name as parameter,'
                                                                 ' s.name as subparameter,t.name as taluk from ra_main v, ra_sub_parameter s,ra_parameter p,'
                                                                 ' ra_category c, ra_taluk t, ra_year y where v.taluk_id=' + talukId + ' and v.year_id=y.id and v.taluk_id=t.id'
                                                                 ' and v.sub_parameter_id=s.id and s.parameter_id=p.id and c.id=p.category_id')
        elif talukId == '0':
            if subparameterId != '0':
                logger.error('Hello13')
                value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, s.name as subparameter,t.name as taluk from ra_main v,'
                                                         ' ra_sub_parameter s, ra_taluk t, ra_year y where v.sub_parameter_id=' + subparameterId + ' and v.year_id=y.id and'
                                                         ' v.taluk_id=t.id and v.sub_parameter_id=s.id')
            elif subparameterId == '0':
                if parameterId != '0':
                    logger.error('Hello14')
                    value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, p.name as parameter, s.name as subparameter,t.name'
                                                             ' as taluk from ra_main v, ra_sub_parameter s, ra_parameter p, ra_taluk t, ra_year y '
                                                             'where p.id=' + parameterId + ' and v.year_id=y.id and v.taluk_id=t.id and v.sub_parameter_id=s.id  and'
                                                             ' s.parameter_id=p.id')
                elif parameterId == '0':
                    if categoryId != '0':
                        logger.error('Hello15')
                        value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, c.name as category, p.name as parameter,'
                                                                 ' s.name as subparameter,t.name as taluk from ra_main v, ra_sub_parameter s,'
                                                                 ' ra_parameter p, ra_category c, ra_taluk t, ra_year y where c.id=' + categoryId + ' and'
                                                                 ' v.year_id=y.id and v.taluk_id=t.id and v.sub_parameter_id=s.id  and '
                                                                 's.parameter_id=p.id and p.category_id=c.id')
                    elif categoryId == '0':
                        logger.error('Hello16')
                        value_objects = RaCustomMain.objects.raw('select v.id, v.value, y.name as year, c.name as category, p.name as parameter, s.name'
                                                                 ' as subparameter,t.name as taluk from ra_main v, ra_sub_parameter s, ra_parameter p, '
                                                                 'ra_category c, ra_taluk t, ra_year y where v.year_id=y.id and v.taluk_id=t.id and '
                                                                 'v.sub_parameter_id=s.id  and s.parameter_id=p.id and p.category_id=c.id')

        # value_objects = RaMain.objects.filter(sub_parameter=subparameterId).filter(taluk=talukId).filter(year__in=[1,2])
    lis = []
    for value_object in value_objects:
        dic = dict(value_object.__dict__)
        del dic['_state']
        lis.append(dic)
    return HttpResponse(json.dumps(lis), content_type="application/json")

@api_view(['GET'])
def value(request, value_id):
    value_object = RaMain.objects.get(id=value_id)
    return Response(RaMainSerializer(value_object).data)

# @api_view(['GET'])
# def template(request):
#     data = {'YearOpts': RaYearSerializer().data, 'CategoryOpts': RaCategorySerializer().data,
#             'ParameterOpts': RaParameterSerializer().data}
#     return Response(data)

