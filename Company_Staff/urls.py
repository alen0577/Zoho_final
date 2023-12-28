from django.urls import path
from . import views

urlpatterns = [
    path('Company-Dashboard/<int:pk>',views.company_dashboard,name='company_dashboard'),
    path('Staff-Dashboard/<int:pk>',views.staff_dashboard,name='staff_dashboard')
  
    
]