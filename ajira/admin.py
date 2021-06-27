# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Employee, EmployeeSalary, Leave, Profile

# Register your models here.
admin.site.register(Profile)
admin.site.register(Employee)
admin.site.register(EmployeeSalary)
admin.site.register(Leave)
