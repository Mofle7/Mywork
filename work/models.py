from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm


class Profile(models.Model):
    user = models.OneToOneField (User)
    name = models.CharField(max_length=40)
    mobile = models.CharField(max_length = 10)

class Worker(models.Model):
    user = models.OneToOneField (User)
    image = models.FileField(upload_to='profile_image')
    worker_services = models.TextField()
    worker_experince = models.TextField()
    creat_date = models.DateTimeField(auto_now_add=True)


class Adv(models.Model):
    user = models.ForeignKey(User)
    adv_text = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)







# Create your models here.
# Create your models here.
