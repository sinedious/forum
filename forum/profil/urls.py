from django.urls import path
from profil import views

urlpatterns = [
    path('',views.changeData,name='profil')
]