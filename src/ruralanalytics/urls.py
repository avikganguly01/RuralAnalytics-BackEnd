from django.conf.urls import url, patterns, include
from rest_framework import viewsets
from ra import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = [

     
	 url(r'^ra/template$',views.template,name='template'),
	 url(r'^ra/subparameters/(?P<parameter_id>\d+)/',views.subparameters, name='subparameters')
]

