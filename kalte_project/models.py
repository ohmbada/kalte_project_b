from django.db import models
from django.contrib.auth.models import User

class Users(models.Model):
    name = models.CharField(max_length=4)
    email = models.EmailField()
    borndate = models.DateField()
    phone = models.TextField(max_length=13)

# class Restaurant(models.Model):
#     title = models.TextField()
#     address = models.TextField()
#     phone = models.TextField()
#     account = models.TextField()
