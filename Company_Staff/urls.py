from django.urls import path
from . import views

urlpatterns = [
    path('Staff-Dashboard/<int:pk>',views.staff_dashboard,name='staff_dashboard')
  
    
]