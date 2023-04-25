from django.db import models
from django.core.validators import MinLengthValidator

class Feedback(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField(validators=[MinLengthValidator(15)])
    pub_date = models.DateTimeField(auto_now_add=True) ## wird nicht angezeigt Xd?
    
    def __str__(self):
        return self.title
