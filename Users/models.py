
from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class UserCustom(models.Model):
    name = models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(max_length=255,unique=True,blank=True,null=True)
    password = models.CharField(max_length=255,blank=True,null=True)
    fulladdress = models.CharField(max_length=250,blank=True,null=True)
    phone = models.CharField(max_length=255,unique=True)
    code = models.CharField(max_length=255,blank=True,null=True)

    def __str__(self):
        return self.phone

    def __unicode__(self):
        return self.phone,self.email
