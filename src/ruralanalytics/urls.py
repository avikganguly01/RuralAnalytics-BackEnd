from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from ra.views.views import *

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [

    # url(r'^ra/template$', template, name='template'),
    url(r'^ra/categories$', categories, name='categories'),
    url(r'^ra/categories/(?P<category_id>\d+)', category, name='category'),
    url(r'^ra/parameters$', parameters, name='parameters'),
    url(r'^ra/parameters/(?P<parameter_id>\d+)', parameter, name='parameter'),
    url(r'^ra/subparameters$', subparameters, name='subparameters'),
    url(r'^ra/subparameters/(?P<subparameter_id>\d+)', subparameter, name='subparameter'),
    url(r'^ra/years$', years, name='years'),
    url(r'^ra/years/(?P<year_id>\d+)', year, name='year'),
    url(r'^ra/taluks$', taluks, name='taluks'),
    url(r'^ra/taluks/(?P<taluk_id>\d+)', taluk, name='taluk'),
    url(r'^ra/districts$', districts, name='districts'),
    url(r'^ra/districts/(?P<district_id>\d+)', district, name='district'),
    url(r'^ra/values$', values, name='values'),
    url(r'^ra/values/(?P<value_id>\d+)', value, name='value')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

