from re import T
from django.shortcuts import render

# Create your views here.

from django.views.decorators.csrf import csrf_exempt
#library ini buat allow other domains to access our api

from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
#to parse incomeing data into data model

from data_collector.models import Departments,Employees
#import model yang udah dibuat

from data_collector.serializers import DepartmentsSerializer,EmployeeSerializer
#import juga serializers nya bruh

from django.core.files.storage import default_storage
#untuk safe file photo nya


@csrf_exempt
#method akan menerima optional id yang akan digunakan pada delete method
def departmentApi(request,id=0):
    #GET methode akan return in json format
    if request.method=='GET':
        departments = Departments.objects.all()
        #pake serializers class buat convert ke json nya bruh
        departments_serializer = DepartmentsSerializer(departments, many=True)
        #return safe=false disini while trying to convert to django, lamun aya issue diabaikan
        return JsonResponse(departments_serializer.data, safe=False)
    elif request.method=='POST':
        department_data = JSONParser().parse(request)
        #serializer untuk convert ke model
        departments_serializer = DepartmentsSerializer(data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse('Penambahan data sukses', safe=False)
        return JsonResponse('Penambahan gagal', safe=False)
    elif request.method=='PUT':
        department_data=JSONParser().parse(request)
        department=Departments.objects.get(DepartmentId=department_data['DepartmentId'])
        departments_serializer = DepartmentsSerializer(department,data=department_data)
        if departments_serializer.is_valid():
            departments_serializer.save()
            return JsonResponse("update data sukses",safe=False)
        return JsonResponse("update gagal")
    elif request.method=='DELETE':
        department = Departments.objects.get(DepartmentId=id)
        department.delete()
        return JsonResponse("Delete data sukses", safe=False)


@csrf_exempt     
def employeeApi(request,id=0):
    if request.method=='GET':
        pekerja = Employees.objects.all()
        pekerja_serializer = EmployeeSerializer(pekerja, many=True)
        return JsonResponse(pekerja_serializer.data, safe=False)
    if request.method=='POST':
        pekerja_data = JSONParser().parse(request)
        pekerja_serializer = EmployeeSerializer(data = pekerja_data)
        if pekerja_serializer.is_valid():
            pekerja_serializer.save()
            return JsonResponse("penambahan data sukses", safe=False)
        return JsonResponse("Penambahan gagal", safe=False)
    if request.method=='PUT':
        pekerja_data = JSONParser().parse(request)
        pekerja = Employees.objects.get(EmployeeId = pekerja_data['EmployeeId'])
        pekerja_serializer = EmployeeSerializer(pekerja, data = pekerja_data)
        if pekerja_serializer.is_valid():
            pekerja_serializer.save()
            return JsonResponse("Update pekerja sukses", safe=False)
        return JsonResponse("Update pekerja gagal")
    if request.method=="DELETE":
        pekerja = Employees.objects.get(EmployeeId=id)
        pekerja.delete()
        return JsonResponse("Delete Pekerja sukses", safe=False)

@csrf_exempt
def SaveFile(request,id=0):
    file = request.FILES['file']
    file_name=default_storage.save(file.name,file)
    return JsonResponse(file_name, safe=False)
    