from django.db import models
from django.contrib.auth.models import User

class register(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.user.username