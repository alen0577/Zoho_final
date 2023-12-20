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

def company_register_page(request):
  return render(request, 'company_register.html')

def company_register2(request):
  terms=payment_terms.objects.all()
  context={
    'terms':terms
  }
  return render(request,'company_register2.html', context) 


def staff_register_page(request):
  return render(request, 'staff_register.html')


def login_page(request):
  return render(request, 'login.html')
