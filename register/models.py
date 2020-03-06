from django.db import models

# Create your models here.
class CrudUser(models.Model):
    name = models.CharField(max_length=30, blank=True)
    address = models.CharField(max_length=100, blank=True)
    age = models.IntegerField(blank=True, null=True)

class CrudUserRegister(models.Model):
    firstname = models.CharField(max_length=100, blank=True)
    lastname = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=50, blank=True, )    
    mobile = models.CharField(max_length=100, blank=True)
    password=models.CharField(max_length=50, blank=True, )    