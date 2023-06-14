from django.db import models
from django.contrib.auth.models import User

class beitrag(models.Model):
    titel = models.CharField(max_length=100)
    beitrag = models.CharField(max_length=500)
    likes = models.ManyToManyField(User, related_name='liked_beitraege', blank=True)
    image = models.ImageField(upload_to="static/test", null=True, blank=True)

    def str(self):
        return self.titel

    def get_like_count(self):
        return self.likes.count()
    
class comment(models.Model):
    beitrag = models.ForeignKey(beitrag, related_name="comments", on_delete=models.CASCADE)
    Kommentar = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self) ->str:
        return '%s - %s' % (self.beitrag.titel, self.author)