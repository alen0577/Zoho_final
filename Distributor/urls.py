from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [

    path('Distributor_Dashboard\<int:pk>',views.distributor_dashboard,name='distributor_dashboard'),
    path('Dist_clients',views.dist_clients,name='dist_clients'),
    path('Dist_Client_Requests',views.dist_client_requests,name='dist_client_requests'),
    path('Dist_Client_Accept\<int:id>',views.dist_client_accept,name='dist_client_accept'),
    path('Dist_Client_Reject\<int:id>',views.dist_client_reject,name='dist_client_reject'),
    path('Dist_Client_Request_Overview\<int:id>',views.dist_client_request_overview,name='dist_client_request_overview'),
    path('All_Clients',views.all_clients,name='all_clients'),
    path('Client_Details\<int:id>',views.client_details,name='client_details'),

   
  
   
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)