from django.urls import path
from login_register import views


urlpatterns = [
    path('', views.user_login, name='login'),  
    path('register/', views.register, name='register'),
    path('logout', views.user_logout, name='logout'),
    
    
]