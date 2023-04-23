from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinLengthValidator

class beitrag(models.Model):
    titel = models.CharField(max_length=100)
    beitrag = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.titel
    

class register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username
    
class Feedback(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(15)])
    pub_date = models.DateTimeField(auto_now_add=True) ## wird nicht angezeigt Xd?
    
    def __str__(self):
        return self.title
    