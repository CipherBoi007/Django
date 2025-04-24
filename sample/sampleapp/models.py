from django.db import models

# Create your models here.
class Data(models.Model):
    Name = models.CharField(max_length=10,default="")
    Email = models.CharField(max_length=10,default="")
    Message = models.CharField(max_length=100,default="")