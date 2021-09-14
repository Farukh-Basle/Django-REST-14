

from django.shortcuts import render,redirect
from TokenAuthentication_App.models import Employee
from TokenAuthentication_App.api.serializers import EmployeeSerializer
from rest_framework.viewsets import ModelViewSet

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAdminUser



class EmployeeModelViewSet(ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

    authentication_classes = (TokenAuthentication,)
    permission_classes = (IsAdminUser,)







