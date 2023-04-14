from django.db import models
from django.contrib.auth.models import User

class beitrag(models.Model):
    titel = models.CharField(max_length=100)
    beitrag = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.titel
    

class register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
