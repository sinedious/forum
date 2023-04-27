from django.urls import path
from message import views

urlpatterns = [
      path('', views.inbox, name='inbox'),
      path('send_Message/', views.send_message, name='send_message') 
    
]