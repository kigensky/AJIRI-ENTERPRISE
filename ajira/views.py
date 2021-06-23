# -*- coding: utf-8 -*-
from rest_framework import response
from ajira.serializers import UserSerializer
from rest_framework import serializers
from rest_framework.views import APIView  
from .serializers import UserSerializer
from rest_framework.response import Response
from rest_framework.exceptions import AuthenticationFailed
from .models import User
import jwt, datetime
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
class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class LoginView(APIView):
    def post(self, request):
        email = request.data['email']
        password = request.data['password']


        user = User.objects.filter(email=email).first()

        if user is None:
            raise AuthenticationFailed('User not found!')
        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password!')
        payload = {
            'id': user.id,
            'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=60),
            'iat': datetime.datetime.utcnow()
        }

        token =  jwt.encode(payload, 'secret', algorithm='HS256').decode('utf-8')

        respone = Response()

        respone.set_cookie(key='jwt', value=token, httponly=True)

        respone.data = {
            'jwt': token
        }


        return respone

class UserView(APIView):

    def get(self, request):
        token = request.COOKIES.get('jwt')

        if not token:
            raise AuthenticationFailed('Unauthenticated!')

        try:
            payload = jwt.decode(token, 'secret', algorithm=['HS256'])
        except jwt.ExpiredSignatureError:
            raise AuthenticationFailed('Unauthenticated!')

        user = User.objects.filter(id=payload['id']).first()
        serializer = UserSerializer(user)
        return Response(serializer.data)

class LogoutView(APIView):
    def post(self, request):
        response = Response()
        response.delete_cookie('jwt')
        response.data = {
            'message': 'success'
        }

        return response

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