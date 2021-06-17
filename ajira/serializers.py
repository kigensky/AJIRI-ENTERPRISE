from django.db import models
from django.db.models import fields
from .models import  Employees
from rest_framework import serializers
from django import forms


class EmployeesSerializers(serializers.ModelSerializer):
  class Meta:
    model = Employees
    fields = "__all__"
