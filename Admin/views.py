from datetime import date, timedelta
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from Register_Login.models import *
from django.contrib import messages
from django.http import JsonResponse


# Create your views here.

@login_required(login_url='login_page')
def admindash(request):
  return render(request, 'admindash.html')

@login_required(login_url='login_page')
def payment_terms(request):
  terms = PaymentTerms.objects.all()
  return render(request,'payment_terms.html',{'terms':terms})

@login_required(login_url='login_page')
def add_payment_terms(request):
  if request.method == 'POST':
    num=int(request.POST['num'])
    select=request.POST['select']
    if select == 'Years':
      days=int(num)*365
      pt = PaymentTerms(payment_terms_number = num,payment_terms_value = select,days = days)
      pt.save()
      messages.info(request, 'Payment term is added!')
      return redirect('payment_terms')

    else:  
      days=int(num*30)
      pt = PaymentTerms(payment_terms_number = num,payment_terms_value = select,days = days)
      pt.save()
      messages.success(request, 'Payment term is added !')
      return redirect('payment_terms')


  return redirect('payment_terms')

@login_required(login_url='login_page')
def remove_payment_terms(request,pk):
  payment_term=PaymentTerms.objects.get(id=pk)
  payment_term.delete()
  messages.success(request, 'Payment term is removed !')
  return redirect('payment_terms')



#distributor approval section----------------------------

@login_required(login_url='login_page')
def admin_distributors(request):
    return render(request,'distributors.html')

@login_required(login_url='login_page')
def distributor_requests(request):
  
  distributors = DistributorDetails.objects.filter(superadmin_approval=0).order_by('-id')
  return render(request,'distributor_requests.html',{'distributors':distributors})

def admin_distributor_accept(request,id):
  data=DistributorDetails.objects.filter(id=id).update(superadmin_approval=1)
  return redirect('distributor_requests')

def admin_distributor_reject(request,id):
  data=DistributorDetails.objects.get(id=id)
  data.login_details.delete()
  data.delete()
  return redirect('distributor_requests')

@login_required(login_url='login_page')
def distributor_request_overview(request,id):
  data=DistributorDetails.objects.get(id=id)
  return render(request,'distributor_request_overview.html',{'distributor_details':data})

@login_required(login_url='login_page')
def all_distributors(request):
  distributors=DistributorDetails.objects.filter(superadmin_approval=1)
  return render(request,'all_distributors.html',{'distributors':distributors})

@login_required(login_url='login_page')
def distributor_details(request,id):
  data=DistributorDetails.objects.get(id=id)
  return render(request,'distributor_details.html',{'distributor_details':data})

def admin_distributor_cancel(request,id):
  data=DistributorDetails.objects.filter(id=id).update(superadmin_approval=0)
  return redirect('all_distributors')

@login_required(login_url='login_page')
def clients_under_distributor(request):
  distributors=DistributorDetails.objects.filter(superadmin_approval=1)
  context={
    'distributors':distributors
  }
  return render(request,'clients_Under_distributor.html',context)

# distributor  wise client details---------------------------------

def get_clients_under_distributor(request):
  if request.method == 'GET':
    distributor_id = request.GET.get('distributor_id')
    

    # Query your database to fetch employee details based on the employee_id.

    company = CompanyDetails.objects.filter(distributor=distributor_id,superadmin_approval=1,Distributor_approval=1).order_by('-id')
    company_details=[]

    for i in company:
      cmp_id=i.id
      name=i.company_name
      email=i.login_details.email
      contact=i.contact
      pterm_no=i.payment_term.payment_terms_number
      pterm_value=i.payment_term.payment_terms_value
      sdate=i.start_date
      edate=i.End_date

      company_details.append({
        'cmp_id':cmp_id,
        'name':name,
        'email':email,
        'contact':contact,
        'pterm_no':pterm_no,
        'pterm_value':pterm_value,
        'sdate':sdate,
        'edate':edate
      })
    
    # You might want to serialize the 'company_details' to a JSON format.
    return JsonResponse({'details': company_details})

  else:
    return JsonResponse({'error': 'Invalid request method.'}, status=400)

@login_required(login_url='login_page')
def distributor_client_profile_details(request,pk):
  company = CompanyDetails.objects.get(id=pk)
  allmodules=ZohoModules.objects.get(company=company,status='New')
 

  context={
    'details':company,
    'allmodules':allmodules
  }

  return render(request,'distributor_client_profile_details.html',context)




#client approval section----------------------------

@login_required(login_url='login_page')
def admin_clients(request):
    return render(request,'clients.html')

@login_required(login_url='login_page')
def client_requests(request):
  
  clients = CompanyDetails.objects.filter(superadmin_approval=0,reg_action='self').order_by('-id')
  return render(request,'client_requests.html',{'clients':clients})


def admin_client_accept(request,id):
  data=CompanyDetails.objects.filter(id=id).update(superadmin_approval=1)
  return redirect('client_requests')

def admin_client_reject(request,id):
  data=CompanyDetails.objects.get(id=id)
  data.login_details.delete()
  data.delete()
  return redirect('client_requests')

@login_required(login_url='login_page')
def client_request_overview(request,id):
  data=CompanyDetails.objects.get(id=id)
  allmodules=ZohoModules.objects.get(company=data,status='New')
  return render(request,'client_request_overview.html',{'company':data,'allmodules':allmodules})

@login_required(login_url='login_page')
def all_clients(request):
  clients=CompanyDetails.objects.filter(superadmin_approval=1,reg_action='self')
  return render(request,'all_clients.html',{'clients':clients})

@login_required(login_url='login_page')
def client_details(request,id):
  data=CompanyDetails.objects.get(id=id)
  allmodules=ZohoModules.objects.get(company=data,status='New')
  return render(request,'client_details.html',{'company':data,'allmodules':allmodules})

def admin_client_cancel(request,id):
  data=CompanyDetails.objects.filter(id=id).update(superadmin_approval=0)
  return redirect('all_clients')

# Admin notifications------------------------------------

@login_required(login_url='login_page')
def admin_notification(request):

  companies = CompanyDetails.objects.filter(reg_action='self')

  for c in companies:
    c.days_remaining = (c.End_date - date.today()).days
    print(c.days_remaining)

  distributor = DistributorDetails.objects.all()

  for d in distributor:
    d.days_remaining = (d.End_date - date.today()).days
    print(d.days_remaining)


  pterm_updation = PaymentTermsUpdates.objects.filter(update_action=1,status='Pending')
  data= ZohoModules.objects.filter(update_action=1,status='Pending')
  return render(request,'admin_notification.html',{'data':data,'pterm_updation':pterm_updation,'companies':companies,'distributor':distributor})



@login_required(login_url='login_page')
def module_updation_details(request, mid):
  data = ZohoModules.objects.get(id=mid)
  allmodules = ZohoModules.objects.filter(company=data.company,update_action=1, status='Pending')
  old_modules = ZohoModules.objects.filter(company=data.company,update_action=0, status='New')

  # Extract the field names related to modules
  module_fields = [field.name for field in ZohoModules._meta.fields if field.name not in ['id', 'company', 'status', 'update_action']]

  # Get the previous and new values for the selected modules
  previous_values = old_modules.values(*module_fields).first()
  new_values = data.__dict__

  # Identify added and deducted modules
  added_modules = {}
  deducted_modules = {}

  for field in module_fields:
    if new_values[field] > previous_values[field]:
      added_modules[field] = new_values[field] - previous_values[field]
    elif new_values[field] < previous_values[field]:
      deducted_modules[field] = previous_values[field] - new_values[field]
  
  new = ZohoModules.objects.filter(company=data.company,update_action=1, status='Pending')
  old = ZohoModules.objects.filter(company=data.company,update_action=0, status='New')

  context = {
    'data': data,
    'allmodules': allmodules,
    'old_modules': old_modules,
    'previous_values': previous_values,
    'new_values': new_values,
    'added_modules': added_modules,
    'deducted_modules': deducted_modules,
    'new':new,
    'old':old,
  }
  
  print(new,old)
  print(added_modules,deducted_modules)

  return render(request, 'module_updation_details.html',context)


def module_updation_ok(request,mid):
  
  old=ZohoModules.objects.get(company=mid,status='New')
  old.delete()

  data=ZohoModules.objects.get(company=mid,status='Pending')  
  data.status='New'
  data.save()
  data1=ZohoModules.objects.filter(company=mid).update(update_action=0)
  return redirect('admin_notification')

@login_required(login_url='login_page')
def pterm_updation_details(request,pid):
  term= PaymentTermsUpdates.objects.get(id=pid)
  new_term= PaymentTermsUpdates.objects.get(company=term.company,status='Pending')
  old_term = PaymentTermsUpdates.objects.get(company=term.company,status='New')
  start_date = term.company.start_date
  end_date = term.company.End_date 
  current_date = date.today()
  difference_in_days = (end_date - current_date).days
  print(term)
  print(new_term)
  print(old_term)

  context = {
    'new_term':new_term,
    'old_term':old_term,
    'term':term,
    'difference_in_days':difference_in_days
    }
  return render(request,'pterm_updation_details.html',context)

def pterm_updation_ok(request,cid):
  
  old_term=PaymentTermsUpdates.objects.get(company=cid,status='New')
  old_term.delete()

  new_term=PaymentTermsUpdates.objects.get(company=cid,status='Pending')  
  new_term.status='New'
  new_term.update_action=0
  new_term.save()

  terms = new_term.payment_term

  start_date=date.today()
  days=int(terms.days)
    
  end= date.today() + timedelta(days=days)
  End_date=end
  
  company = CompanyDetails.objects.get(id=cid)
  company.payment_term=terms
  company.start_date=start_date
  company.End_date=End_date
  company.save()
  return redirect('admin_notification')

@login_required(login_url='login_page')
def dist_pterm_updation_details(request,pid):
  term= PaymentTermsUpdates.objects.get(id=pid)
  new_term= PaymentTermsUpdates.objects.get(company=term.company,status='Pending')
  old_term = PaymentTermsUpdates.objects.get(company=term.company,status='New')
  start_date = term.distributor.start_date
  end_date = term.distributor.End_date 
  current_date = date.today()
  difference_in_days = (end_date - current_date).days
  print(term)
  print(new_term)
  print(old_term)

  context = {
    'new_term':new_term,
    'old_term':old_term,
    'term':term,
    'difference_in_days':difference_in_days
    }
  return render(request,'dist_pterm_updation_details.html',context)

def dist_pterm_updation_ok(request,cid):
  
  old_term=PaymentTermsUpdates.objects.get(distributor=cid,status='New')
  old_term.delete()

  new_term=PaymentTermsUpdates.objects.get(distributor=cid,status='Pending')  
  new_term.status='New'
  new_term.update_action=0
  new_term.save()

  terms = new_term.payment_term

  start_date=date.today()
  days=int(terms.days)
    
  end= date.today() + timedelta(days=days)
  End_date=end
  
  distributor = DistributorDetails.objects.get(id=cid)
  distributor.payment_term=terms
  distributor.start_date=start_date
  distributor.End_date=End_date
  distributor.save()
  return redirect('admin_notification')


  
  