from django.shortcuts import render
from rest_framework import viewsets
from api.models import company,Employee
from api.serializers import companySerializer,EmployeeSerializer

# Create your views here.
class companyViewSet(viewsets.ModelViewSet):
    queryset=company.objects.all()
    serializer_class=companySerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset=Employee.objects.all()
    serializer_class=EmployeeSerializer