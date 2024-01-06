from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [


    # Payment term section----------------------------
    path('Payment_Terms',views.payment_terms,name='payment_terms'),
    path('Add/Payment_Terms',views.add_payment_terms,name='add_payment_terms'),
    path('Remove/Payment_Terms<int:pk>',views.remove_payment_terms,name='remove_payment_terms'),

    # distributor approval section----------------------------

    path('Admin/Dashboard',views.admindash,name='admindash'),
    path('Admin_Distributors',views.admin_distributors,name='admin_distributors'),
    path('Distributor_Requests',views.distributor_requests,name='distributor_requests'),
    path('Admin/Distributor_Accept\<int:id>',views.admin_distributor_accept,name='admin_distributor_accept'),
    path('Admin/Distributor_Reject\<int:id>',views.admin_distributor_reject,name='admin_distributor_reject'),
    path('Distributor_Request_Overview\<int:id>',views.distributor_request_overview,name='distributor_request_overview'),
    path('All_Distributors',views.all_distributors,name='all_distributors'),
    path('Distributor_Details\<int:id>',views.distributor_details,name='distributor_details'),
    path('Admin/Distributor_Cancel\<int:id>',views.admin_distributor_cancel,name='admin_distributor_cancel'),
    
    # client approval section----------------------------

    path('Admin/clients',views.admin_clients,name='admin_clients'),
    path('Client_Requests',views.client_requests,name='client_requests'),
    path('Admin/Client_Accept\<int:id>',views.admin_client_accept,name='admin_client_accept'),
    path('Admin/Client_Reject\<int:id>',views.admin_client_reject,name='admin_client_reject'),
    path('Client_Request_Overview\<int:id>',views.client_request_overview,name='client_request_overview'),
    path('All_Clients',views.all_clients,name='all_clients'),
    path('Client_Details\<int:id>',views.client_details,name='client_details'),
    path('Admin/Client_Cancel\<int:id>',views.admin_client_cancel,name='admin_client_cancel'),

    # Admin notifications------------------------------------

    path('Admin/Notification',views.admin_notification,name='admin_notification'),
    path('Module/Updation_Details\<int:mid>',views.module_updation_details,name='module_updation_details'),
    path('Module/Updation_Ok\<int:mid>',views.module_updation_ok,name='module_updation_ok'),

    path('Pterm/Updation_Details\<int:pid>',views.pterm_updation_details,name='pterm_updation_details'),
    path('Pterm/Updation_Ok\<int:cid>',views.pterm_updation_ok,name='pterm_updation_ok'),

    path('Dist/Pterm_Updation_Details\<int:pid>',views.dist_pterm_updation_details,name='dist_pterm_updation_details'),
    path('Dist/Pterm_Updation_Ok\<int:cid>',views.dist_pterm_updation_ok,name='dist_pterm_updation_ok'),
   

   
    
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)