from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import *
from .serializers import *
from rest_framework import status
from django.http import response
from django.http import Http404

# Create your views here.


class EmployeeList(APIView):
    serializer_class = EmployeesSerializers

    def get_employee(self,pk):
        try:
            return Employees.objects.get(pk=pk)
        except Employees.DoesNotExist:
            return Http404()


    
    def get(self, request, format=None):
        employees = Employees.objects.all()
        serializers = self.serializer_class(employees, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            employees = serializers.data
            response = {
                'data': {
                    'employees': dict(employees),
                    'status':'success',
                    'message': 'employee created successfully ',
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_employee(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTEN