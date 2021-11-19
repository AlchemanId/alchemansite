#basically help to convert the complex types or model instances
#into nativepython data types that can then be easily
# rendered into jso or xml or other content type

from rest_framework import serializers
from data_collector.models import Departments,Employees

class DepartmentsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Departments
        fields=('DepartmentId', "DepartmentName")

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Employees
        fields=('EmployeeId','EmployeeName','Department','DateOfJoining','PhotoFileName')
                