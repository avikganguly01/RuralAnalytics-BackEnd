from __future__ import unicode_literals

from django.db import models

class RaCategory(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    class Meta:
        managed = False
        db_table = 'ra_category'

class RaDistrict(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    class Meta:
        managed = False
        db_table = 'ra_district'

class RaMain(models.Model):
    id = models.IntegerField(primary_key=True)
    year = models.ForeignKey('RaYear')
    taluk = models.ForeignKey('RaTaluk')
    sub_parameter = models.ForeignKey('RaSubParameter')
    value = models.IntegerField(blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'ra_main'

class RaParameter(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    category = models.ForeignKey(RaCategory)
    class Meta:
        managed = False
        db_table = 'ra_parameter'

class RaSubParameter(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=45)
    parameter = models.ForeignKey(RaParameter)
    class Meta:
        managed = False
        db_table = 'ra_sub_parameter'

class RaTaluk(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=45)
    district = models.ForeignKey(RaDistrict)
    class Meta:
        managed = False
        db_table = 'ra_taluk'

class RaYear(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.IntegerField(unique=True)
    class Meta:
        managed = False
        db_table = 'ra_year'
