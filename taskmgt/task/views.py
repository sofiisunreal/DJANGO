from django.shortcuts import render

from rest_framework import viewsets, generics

from .models import Task, Employee , Client
from .serializers import EmployeeSerializer, TaskSerializer, ClientSerializer ,WorkerSerializer
# Create your views here.
# department view sets 
class TaskViewSet(viewsets.ModelViewSet):
    queryset=Task.objects.all()
    serializer_class=TaskSerializer

# generic views 
# employees
# handles the get and post
class EmployeeListView(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer

class WorkerListView(generics.ListCreateAPIView):
    queryset=Employee.objects.all()
    serializer_class=WorkerSerializer

# get one/PUT/delete
class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset=Employee.objects.all()
    serializer_class=WorkerSerializer

class ClientDetailView(generics.RetrieveDestroyAPIView):
    queryset=Client.objects.all()
    serializer_class=ClientSerializer




                             