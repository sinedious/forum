from django.db import models

class Topic(models.Model):
    top_name = models.CharField(max_length=264,unique=True)

    def __str__(self) -> str:
        return self.top_name
    
class Webpage(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.PROTECT)
    name = models.CharField(max_length=264,unique=True)
    url = models.URLField(unique=True)

    def __str__(self) -> str:
        return self.name
    
class AccessRecord(models.Model):
    name = models.ForeignKey(Webpage, on_delete=models.PROTECT)
    date = models.DateField()

    def __str__(self) -> str:
        return str(self.date)
    
class Users_test(models.Model):
    name = models.CharField(max_length=264, unique=True)
    last = models.CharField(max_length=20, unique=True)
    mail = models.EmailField(max_length=50)

    def __str__(self) -> str:
        return self.name

    

