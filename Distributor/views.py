from datetime import date, timedelta
from django.contrib import messages
from django.shortcuts import redirect, render
from django.utils.crypto import get_random_string
from Register_Login.models import *

# Create your views here.

def distributor_dashboard(request,pk):
    dash_details = DistributorDetails.objects.get(id=pk,superadmin_approval=1)
    context = {
        'distributor_details': dash_details
    }
    return render(request, 'distributor_dash.html', context)

def dist_clients(request):
    return render(request,'dist_clients.html')

def dist_client_requests(request):
    if 'log_id' in request.session:
        if request.session.has_key('log_id'):
            log_id = request.session['log_id']
            
        else:
            return redirect('/')  
        log_det = LoginDetails.objects.get(id=log_id)
        distributor_det = DistributorDetails.objects.get(login_details=log_det)
        clients = CompanyDetails.objects.filter(Distributor_approval=0,distributor=distributor_det).order_by('-id')
    return render(request,'dist_client_requests.html',{'clients':clients})

def dist_client_accept(request,id):
  data=CompanyDetails.objects.filter(id=id).update(Distributor_approval=1)
  return redirect('dist_client_requests')

def dist_client_reject(request,id):
  data=CompanyDetails.objects.get(id=id)
  data.login_details.delete()
  data.delete()
  return redirect('dist_client_requests')

def dist_client_request_overview(request,id):
  data=CompanyDetails.objects.get(id=id)
  return render(request,'dist_client_request_overview.html',{'company':data})

def all_clients(request):
  if 'log_id' in request.session:
        if request.session.has_key('log_id'):
            log_id = request.session['log_id']
            
        else:
            return redirect('/')  
        log_det = LoginDetails.objects.get(id=log_id)
        distributor_det = DistributorDetails.objects.get(login_details=log_det)
  clients=CompanyDetails.objects.filter(Distributor_approval=1,distributor=distributor_det)
  return render(request,'all_clients.html',{'clients':clients})

def client_details(request,id):
  data=CompanyDetails.objects.get(id=id)
  return render(request,'client_details.html',{'data':data})

