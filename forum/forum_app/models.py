from django.db import models
from django.contrib.auth.models import User


class beitrag(models.Model):
    titel = models.CharField(max_length=100)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    beitrag = models.CharField(max_length=500)
    def __str__(self):
        return self.titel + ' | ' + str(self.author)
    
    

    