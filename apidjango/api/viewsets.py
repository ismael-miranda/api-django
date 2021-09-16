from rest_framework import viewsets
from apidjango.models import Employee
from apidjango.api.serializer import EmployeeSerializer


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
