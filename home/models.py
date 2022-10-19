from __future__ import absolute_import
from distutils.command.upload import upload
from email.mime import image
from time import time
from django.db import models

# Create your models here.

class Event(models.Model):
    sr_no = models.AutoField(primary_key=True) 
    name=models.CharField(max_length=30)
    about=models.TextField(max_length=500)
    time=models.DateTimeField()
    location=models.CharField(max_length=200)
    image=models.ImageField(upload_to="images/%y",default="")
    is_liked = models.BooleanField(default = False)
    def __str__(self):
        return self.name