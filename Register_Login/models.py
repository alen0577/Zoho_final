from django.db import models

# Create your models here.

# models for distributor, company, staff registration and payment terms

class LoginDetails(models.Model):
    first_name = models.CharField(max_length=100,null=True,blank=True) 
    last_name = models.CharField(max_length=100,null=True,blank=True) 
    email = models.CharField(max_length=100,null=True,blank=True) 
    username = models.CharField(max_length=100,null=True,blank=True) 
    password = models.CharField(max_length=100,null=True,blank=True) 
    user_type = models.CharField(max_length=100,null=True,blank=True) 
    self_distributor = models.CharField(max_length=100,null=True,blank=True,default='self')
    distributor_id = models.CharField(max_length=100,null=True,blank=True,default='')
    company_id = models.CharField(max_length=100,null=True,blank=True,default='')



class PaymentTerms(models.Model):
    payment_terms_number = models.IntegerField(null=True,blank=True)  
    payment_terms_value = models.CharField(max_length=100,null=True,blank=True) 
    days = models.CharField(max_length=100,null=True,blank=True) 


class DistributorDetails(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    payment_term = models.ForeignKey(PaymentTerms, on_delete=models.CASCADE,null=True,blank=True)
    contact = models.CharField(max_length=100,null=True,blank=True) 
    distributor_code = models.CharField(max_length=100,null=True,blank=True) 
    start_date = models.DateField(max_length=255,null=True,blank=True)
    End_date = models.DateField(max_length=255,null=True,blank=True)
    image = models.ImageField(null=True,blank = True,upload_to = 'image/distributor') 
    log_action = models.IntegerField(null=True,default=0)
    superadmin_approval = models.IntegerField(null=True,default=0)


class CompanyDetails(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    distributor = models.ForeignKey(DistributorDetails, on_delete=models.CASCADE,null=True,blank=True)
    payment_term = models.ForeignKey(PaymentTerms, on_delete=models.CASCADE,null=True,blank=True)
    company_name = models.CharField(max_length=100,null=True,blank=True) 
    contact = models.CharField(max_length=100,null=True,blank=True)
    company_code = models.CharField(max_length=100,null=True,blank=True) 
    address = models.CharField(max_length=100,null=True,blank=True)
    city = models.CharField(max_length=100,null=True,blank=True)
    state = models.CharField(max_length=100,null=True,blank=True)
    country = models.CharField(max_length=100,null=True,blank=True)
    contact = models.CharField(max_length=100,null=True,blank=True)
    pincode = models.IntegerField(null=True,blank=True)
    pan_number = models.CharField(max_length=255,null=True,blank=True)
    start_date = models.DateField(max_length=255,null=True,blank=True)
    End_date = models.DateField(max_length=255,null=True,blank=True)
    gst_type = models.CharField(max_length=255,null=True,blank=True)
    gst_no = models.CharField(max_length=255,null=True,blank=True)
    profile_pic = models.ImageField(null=True,blank = True,upload_to = 'image/company')
    superadmin_approval = models.IntegerField(null=True,default=0)  
    Distributor_approval = models.IntegerField(null=True,default=0) 
    reg_action = models.CharField(max_length=255,null=True,blank=True,default='self')


class StaffDetails(models.Model):
    login_details = models.ForeignKey(LoginDetails, on_delete=models.CASCADE,null=True,blank=True)
    company = models.ForeignKey(CompanyDetails, on_delete=models.CASCADE,null=True,blank=True)
    contact = models.CharField(max_length=255,null=True,blank=True)
    image = models.ImageField(null=True,blank = True,upload_to = 'image/staff')    
    company_approval = models.IntegerField(null=True,default=0)    
    position = models.CharField(max_length=255,null=True,blank=True,default='staff')


