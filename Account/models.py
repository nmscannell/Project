from django.db import models

# Create your models here.

class Account(models.Model):
    userName = models.CharField(max_length=20, default=" ")
    name = models.CharField(max_length=20, default=" ")
    password = models.CharField(max_length=20, default="password")
    email = models.EmailField(default="")
    title = models.IntegerField(default=0)
    address = models.CharField(max_length = 50, default=" ")
    officeNumber = models.IntegerField(default=000)
    officePhone = models.CharField(max_length=10, default = "000-000-0000")
    officeDays = models.CharField(max_length=10, default=" ")
    officeHours = models.CharField(max_length=10, default =" ")
    currentUser = models.BooleanField(default=False)

    def __str__(self):
        return self.name



