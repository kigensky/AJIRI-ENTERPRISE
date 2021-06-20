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
        return Response(status=status.HTTP_204_NO_CONTENT)

    
    def put(self, request, name, format=None):
        employee = self.get_employee(name)
        serializers = EmployeesSerializers(employee, request.data)
        if serializers.is_valid():
            serializers.save()
            employee=serializers.data
            response = {
                'data': {
                    'employee': dict(employee),
                    'status': 'success',
                    'message': 'Employee updated successfully',
                }
            }


class SingleEmployeeList(APIView):
     def get(self, request, pk, format=None):
        employee = Employees.objects.get(pk=pk)
        serializers =EmployeesSerializers(employee)
        return Response(serializers.data)

     def delete(self, request, pk, format=None):
        employee = Employees.objects.get(pk=pk)
        serializers =EmployeesSerializers(employee)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class LeaveList(APIView):
    serializer_class = LeaveSerializers

    
    def get(self, request, format=None):
        leave = Leave.objects.all()
        serializers = self.serializer_class(leave, many=True)
        return Response(serializers.data)


    def post(self, request, format=None):
        serializers = self.serializer_class(data=request.data)
        if serializers.is_valid():
            serializers.save()
            leave = serializers.data
            response = {
                'data': {
                    'leave': dict(leave),
                    'status':'success',
                    'message': 'leave created successfully ',
                }
            }
            return Response(response, status=status.HTTP_200_OK)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        employee = self.get_employee(pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class SingleLeaveEmployeeList(APIView):
     def get(self, request, pk, format=None):
        employee = Employees.objects.get(pk=pk)
        serializers =LeaveSerializers(leave)
        return Response(serializers.data)

     def delete(self, request, pk, format=None):
        employee = Employees.objects.get(pk=pk)
        serializers =EmployeesSerializers(employee)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class List(APIView):
  def get_patient(self, pk):
    try:
        return Patient.objects.get(pk=pk)
    except Patient.DoesNotExist:
        return Http404()