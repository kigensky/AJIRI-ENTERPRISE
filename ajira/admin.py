from django.contrib import admin
from .models import Profile,EmployeeSalary,Leave,Employee

admin.site.register(Profile)
admin.site.register(EmployeeSalary)
admin.site.register(Employee)
admin.site.register(Leave)


