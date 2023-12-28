from django.shortcuts import render
from Register_Login.models import *

# Create your views here.

# -------------------------------Company section--------------------------------

def company_dashboard(request,pk):
    dash_details = CompanyDetails.objects.get(id=pk,superadmin_approval=1,Distributor_approval=1)
    allmodules= ZohoModules.objects.get(company=dash_details)
    context = {
        'details': dash_details,
        'allmodules': allmodules
    }
    return render(request, 'company/company_dash.html', context)





# -------------------------------Staff section--------------------------------

def staff_dashboard(request,pk):
    dash_details = StaffDetails.objects.get(id=pk,company_approval=1)
    allmodules= ZohoModules.objects.get(company=dash_details.company)
    context={
        'details':dash_details,
        'allmodules': allmodules,
    }
    return render(request,'staff/staff_dash.html',context)