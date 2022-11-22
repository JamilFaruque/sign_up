from django.db import models

# Create your models here.

class Accounts(models.Model):

    name = models.CharField(max_length=111)
    email = models.EmailField()
    password = models.CharField(max_length=20)
