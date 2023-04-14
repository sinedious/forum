from django.urls import path
from forum_app import views


urlpatterns = [
    path('', views.user_login, name='login'),  
    path('register/', views.register, name='register')  
]
