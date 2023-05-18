from django.urls import path
from forum_app import views
from .views import  BeitragDetail
from .views import like_beitrag


urlpatterns = [
    path('beitrag/<int:pk>/like/', like_beitrag, name='like-beitrag'),
    path('beitrag/<int:pk>/', BeitragDetail.as_view(), name='beitrag-detail'),
]

