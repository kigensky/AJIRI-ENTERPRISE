from django.db import models
from django.db.models import fields
from .models import  Employees,Leave
from rest_framework import serializers
from django import forms


class EmployeesSerializers(serializers.ModelSerializer):
  class Meta:
    model = Employees
    fields = "__all__"


class LeaveSerializers(serializers.ModelSerializer):
  class Meta: 
    model = Leave
    fields = "__all__"


