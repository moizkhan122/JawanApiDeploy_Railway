from django.db import models

# Create your models here.

#company model here
class ProductModel(models.Model):
    product_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2) 
    description=models.TextField()

    def __str__(self) :
        return self.name
    
#UserModel
class UserModel(models.Model):
    User_id=models.AutoField(primary_key=True)
    name=models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    phone=models.CharField(max_length=15)

#cart Model
class CartModel(models.Model):
    Cart_id=models.AutoField(primary_key=True)
    ProductName=models.CharField(max_length=50)
    ProductPrice = models.DecimalField(max_digits=10, decimal_places=2)
    added_date=models.DateTimeField(auto_now=True)


#     #make a link between CompanyModel and Employee Model
    #company = models.ForeignKey(UserModel,on_delete=models.CASCADE)

# #Employee Model
# class EmployeeModel(models.Model):
#     #mployee_id=models.AutoField(primary_key=True)
#     name=models.CharField(max_length=50)
#     email=models.CharField(max_length=50)
#     phone=models.CharField(max_length=10)
#     address=models.CharField(max_length=200)  
#     about=models.TextField()
#     position=models.CharField(max_length=50,choices=
#                             (('Manager','manager'),
#                              ('Software Developer','sd'),
#                              ('Project Leader','pl')
#                              ))
    
#     #make a link between CompanyModel and Employee Model
#     company = models.ForeignKey(CompanyModel,on_delete=models.CASCADE)