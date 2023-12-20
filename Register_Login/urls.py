from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page,name='landing_page'),
    path('Distributor_Register',views.distributor_register_page,name='distributor_register_page'),
    path('Company_Register',views.company_register_page,name='company_register_page'),
    path('Staff_Register',views.staff_register_page,name='staff_register_page'),
    path('Login_Page',views.login_page,name='login_page'),
]