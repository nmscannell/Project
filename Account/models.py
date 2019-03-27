from django.db import models

# Create your models here.


class Account(models.Model):
    Accountname = models.CharField(max_length=20)
    Accountid = models.IntegerField(default=0)



