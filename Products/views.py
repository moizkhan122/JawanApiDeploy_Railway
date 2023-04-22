from django.shortcuts import render
from Products.models import ProductModel,UserModel,CartModel
from Products.serializers import ProductSerializer,UserSerializer,CartSerializer
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
# Create your views here.

class ProductviewSet(viewsets.ModelViewSet):
    queryset = ProductModel.objects.all()
    serializer_class = ProductSerializer

#users viewset
class UserviewSet(viewsets.ModelViewSet):
    queryset = UserModel.objects.all()
    serializer_class = UserSerializer

class CartviewSet(viewsets.ModelViewSet):
    queryset = CartModel.objects.all()
    serializer_class = CartSerializer

            #detail true is for must provide Primary Key
#     @action(detail=True,methods=['get'])
#     def employees(self,request,pk=None):
#         try:
#             company = ProductModel.objects.get(pk=pk)
#             emps=EmployeeModel.objects.filter(company=company)
#             #now creating the obbjext of serializer for serialize the data means format the data in Json Form
#             emps_serializer = EmployeeSerializer(emps,many=True,context={'request':request})
#             return Response(emps_serializer.data)
#         except Exception as e:
#             print(e)
#             return Response({
#                 'Message' : 'Company might not exist'
#             })
# class EmployeeviewSet(viewsets.ModelViewSet):
#     queryset = EmployeeModel.objects.all()
#     serializer_class = EmployeeSerializer
