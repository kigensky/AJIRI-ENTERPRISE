
from django.contrib.auth.models import User
from django.http import response
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from .models import Employee, EmployeeSalary,Profile,Leave
from rest_framework.response import Response
from django.http import Http404
from .serializers import *
from rest_framework import status
from .serializers import EmployeeSerializer, UserSerializer,EmployeeSalarySerializer,ProfileSerializer,LeaveSerializer

# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

class ProfileViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows profile to be viewed or edited.
    """
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class EmployeeSalaryViewset(viewsets.ModelViewSet):
    """
    API endpoint that allows salary to be viewed or edited.
    """
    queryset = EmployeeSalary.objects.all()
    serializer_class = EmployeeSalarySerializer
    permission_classes = [permissions.IsAuthenticated]
    
class EmployeeViewset(viewsets.ModelViewSet):
    """
    API endpoint that lists employees.
    """
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    permission_classes = [permissions.IsAuthenticated]
    
class LeaveViewset(viewsets.ModelViewSet):
    """
    API endpoint shows employees leave dates.
    """
    queryset = Leave.objects.all()
    serializer_class = LeaveSerializer
    permission_classes = [permissions.IsAuthenticated]
