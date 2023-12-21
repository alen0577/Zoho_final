from datetime import date, timedelta
from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from . models import *
from django.contrib import messages
from django.utils.crypto import get_random_string




# Create your views here.
def landing_page(request):
    return render(request,'landpage.html')

def distributor_register_page(request):
  return render(request, 'distributor_register.html')


# Company registration and save

def company_register_page1(request):
  return render(request, 'company_register.html')



def company_register_save1(request):
  if request.method == 'POST':
    # Get data from the form
    first_name = request.POST.get('fname')
    last_name = request.POST.get('lname')
    email = request.POST.get('eid')
    username = request.POST.get('uname')
    password = request.POST.get('pass')
    cpassword = request.POST.get('cpass')
    self_distributor=request.POST.get('self_distributor')
    distributor_id = request.POST.get('did', '')  # It will be an empty string if not provided
    user_type = 'Company'

    if distributor_id != '':
      if DistributorDetails.objects.filter(distributor_code=distributor_id).exists():
        distributor_id=distributor_id
      else :
        messages.info(request, 'Sorry, Distributor id does not exists')
        return redirect('company_register_page1')

    if password == cpassword:
      if LoginDetails.objects.filter(email=email).exists():
        messages.info(request,'Email id exists')
        return redirect('company_register_page1')
      else:
        # Save data to the database
        user = LoginDetails(
          first_name=first_name,
          last_name=last_name,
          email=email,
          username=username,
          password=password,  # Note: Hash the password before saving in a real-world scenario
          user_type=user_type,
          self_distributor=self_distributor,
          distributor_id=distributor_id
        )
        user.save()
        # Redirect to a success page or home page
        return redirect('company_register_page2',user.id)  
    else:
      return redirect('company_register_page1')
  return render(request, 'company_register.html')  

def company_register_page2(request,pk):
  terms=PaymentTerms.objects.all()
  context={
    'terms':terms,
    'company_id':pk
  }
  return render(request,'company_register2.html', context) 

def company_register_save2(request,pk):
  if request.method == 'POST':
    logreg_id=LoginDetails.objects.get(id=pk)
    # Retrieve data from the POST request
    company_name = request.POST.get('cname')
    email = request.POST.get('email')
    address = request.POST.get('address')
    city = request.POST.get('city')
    state = request.POST.get('state')
    country = request.POST.get('country')
    pincode = request.POST.get('pincode')
    pannumber = request.POST.get('pannumber')
    gsttype = request.POST.get('gsttype')
    gstno = request.POST.get('gstno')
    profile_pic=  request.POST.get('gstno')
    # Add more fie lds as needed

    # Create a new CompanyDetails instance and populate it with form data
    company_details_instance = CompanyDetails(
      company_name=company_name,
      email=email,
      address=address,
      city=city,
      state=state,
      country=country,
      pincode=pincode,
      pan_number=pannumber,
      gst_type=gsttype,
      gst_no=gstno,
      # Add more fields as needed
    )

    # Do any additional processing or validation if needed before saving
    # For example, you might want to set the login_details or distributor fields

    company_details_instance.save()  # Save the instance to the database

    return HttpResponse("Data saved successfully!")  # You can customize the response as needed

  return render(request, 'your_template.html')


def staff_register_page(request):
  return render(request, 'staff_register.html')


def login_page(request):
  return render(request, 'login.html')
