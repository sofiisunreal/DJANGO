from django.shortcuts import render
from rest_framework import viewsets, generics

from employees.models import Department, Employee
from employees.serializers import DepartmentSerializer, EmployeeSerializer


# Create your views here.
# department view sets 
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset=Department.objects.all()
    serializer_class=DepartmentSerializer

# generic views 
# employees
# handles the get and post
class EmployeeListCreateView(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

# get one/PUT/delete
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()


                             