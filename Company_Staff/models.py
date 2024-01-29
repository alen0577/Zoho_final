from django.db import models
from Register_Login.models import *

# Create your models here.

#---------------- models for zoho modules--------------------

class Unit(models.Model):
 
    unit_name=models.CharField(max_length=255)
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)


class Chart_of_Accounts(models.Model):
  
    account_type = models.CharField(max_length=255,null=True,blank=True)
    account_name = models.CharField(max_length=255,null=True,blank=True)

    account_description = models.CharField(max_length=255,null=True,blank=True)

    account_number = models.TextField(max_length=255,null=True,blank=True)
    
    account_code = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=255,null=True,blank=True)
    status=models.CharField(max_length=255,null=True,blank=True,default='Active')
    Create_status = models.CharField(max_length=255,null=True,blank=True,default='added')
    company=models.ForeignKey(CompanyDetails,on_delete=models.CASCADE)
    login_details=models.ForeignKey(LoginDetails,on_delete=models.CASCADE)
    sub_account = models.CharField(max_length=255,null=True,blank=True)
    parent_account = models.CharField(max_length=255,null=True,blank=True)