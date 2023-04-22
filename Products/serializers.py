from rest_framework import serializers
from Products.models import ProductModel,UserModel,CartModel

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    product_id=serializers.ReadOnlyField()
    class Meta:
        model=ProductModel
        fields="__all__"

class UserSerializer(serializers.HyperlinkedModelSerializer):
    User_id=serializers.ReadOnlyField()
    class Meta:
        model=UserModel
        fields="__all__"

class CartSerializer(serializers.HyperlinkedModelSerializer):
    Cart_id=serializers.ReadOnlyField()
    class Meta:
        model=CartModel
        fields="__all__"

# class EmployeeSerializer(serializers.HyperlinkedModelSerializer):
#     id=serializers.ReadOnlyField()
#     class Meta:
#         model=ProductModel
#         fields="__all__"