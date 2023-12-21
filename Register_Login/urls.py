from django.urls import path
from . import views

urlpatterns = [
    path('',views.landing_page,name='landing_page'),
    path('Distributor_Register',views.distributor_register_page,name='distributor_register_page'),

    path('Company_Register/Basic_details',views.company_register_page1,name='company_register_page1'),
    path('Company_Register/Company_details/<int:pk>',views.company_register_page2,name='company_register_page2'),
    path('Company_Registration/Save_basic_details',views.company_register_save1,name='company_register_save1'),



    path('Staff_Register',views.staff_register_page,name='staff_register_page'),
    path('Login_Page',views.login_page,name='login_page'),
]