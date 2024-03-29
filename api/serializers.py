from rest_framework import serializers
from api.models import company
from api.models import Employee


class companySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=company
        fields="__all__"


class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model=Employee
        fields="__all__"