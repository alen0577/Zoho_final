from django.shortcuts import render
from Register_Login.models import *

# Create your views here.

# -------------------------------Company section--------------------------------

def company_dashboard(request,pk):
    dash_details = CompanyDetails.objects.get(id=pk,superadmin_approval=1,Distributor_approval=1)
    context = {
        'company_details': dash_details
    }
    return render(request, 'company/company_dash.html', context)





# -------------------------------Staff section--------------------------------

def staff_dashboard(request,pk):
    dash_details = StaffDetails.objects.get(id=pk,company_approval=1)
    context={
        'staff_details':dash_details,
    }
    return render(request,'staff/staff_dash.html',context)