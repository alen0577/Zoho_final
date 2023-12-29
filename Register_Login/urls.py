from django.urls import path
from . import views

urlpatterns = [

    # landing page
    path('',views.landing_page,name='landing_page'),

    # distributor registration
    path('Distributor_Register',views.distributor_register_page,name='distributor_register_page'),

    # company registration
    path('Company_Register/Basic_details',views.company_register_page1,name='company_register_page1'),
    path('Company_Registration/Save_basic_details',views.company_registration_save1,name='company_registration_save1'),
    path('Company_Register/Company_details/<int:pk>',views.company_register_page2,name='company_register_page2'),
    path('Company_Registration/Save_company_details/<int:pk>',views.company_registration_save2,name='company_registration_save2'),

    # staff registration
    path('Staff_Register',views.staff_register_page,name='staff_register_page'),
    path('Staff_Registration',views.staff_registration,name='staff_registration'),

    # modules select section
    path('Modules_Select_Page/<int:pk>',views.modules_select_page,name='modules_select_page'),
    path('Choose_Modules/<int:pk>',views.choose_modules,name='choose_modules'),


    # login section
    path('Login_Page',views.login_page,name='login_page'),
    path('Login',views.login,name='login'),

    # logout section
    path('Logout-User',views.logout,name='logout'),


]