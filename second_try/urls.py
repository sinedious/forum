from django.urls import path
from second_try import views

urlpatterns = [
    path("",views.login,name='login'),
]
