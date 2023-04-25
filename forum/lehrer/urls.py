from django.urls import path
from lehrer import views


urlpatterns = [
    path('', views.lehrer, name='lehrer'),
    path('rules/',views.rules, name="rules")    
]