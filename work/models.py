# -*- coding: utf-8  -*-
from __future__ import unicode_literals
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm
from userena.models import UserenaBaseProfile


class Profile(models.Model,UserenaBaseProfile):
    user = models.OneToOneField (User, unique=True, related_name='profile' ,verbose_name='User Profile')
    name = models.CharField('User Name',max_length=40)
    mobile = models.CharField('user Mobile',max_length = 10)

class Worker(models.Model):
    user = models.OneToOneField (User, verbose_name= 'Worker User')
    image = models.FileField(upload_to='profile image')
    worker_services = models.TextField('Worker Service')
    worker_experince = models.TextField('Worker Experience')
    creat_date = models.DateTimeField(auto_now_add=True)


class Adv(models.Model):
    user = models.ForeignKey(User, verbose_name='Advertise')
    adv_text = models.TextField('Write Your Advertise')
    pub_date = models.DateTimeField(auto_now_add=True)







# Create your models here.
# Create your models here.
