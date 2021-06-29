from django.db.models import fields
from rest_framework import serializers
from .models import User
from .models import Employee, Leave, Profile,EmployeeSalary

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'name', 'email', 'password']
        extra_kwargs = {
            'password':{'write_only': True}
        }

    def create(self, validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance


class ProfileSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Profile
        fields ="__all__"
        
class EmployeeSalarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=EmployeeSalary
        fields= ("employee_name", "salary_date", "salary_amount") 
        
class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Employee
        fields = "__all__"
        
class LeaveSerializer(serializers.HyperlinkedModelSerializer):
    class Meta: 
        model = Leave
        fields = "__all__"       
