from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Profile,EmployeeSalary


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'first_name', 'last_name', 'email', 'groups']

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields ="__all__"

        
class EmployeeSalarySerializer(serializers.ModelSerializer):
    class Meta:
        model=EmployeeSalary
        fields="__all__"