from django.contrib import admin
from django.urls import path,include
from Products.views import ProductviewSet,UserviewSet,CartviewSet
from rest_framework import routers

route = routers.DefaultRouter()
route.register(r'product',ProductviewSet)
route.register(r'users',UserviewSet)
route.register(r'cart',CartviewSet)
# route.register(r'employees',EmployeeviewSet)

urlpatterns = [
    path('',include(route.urls))
]