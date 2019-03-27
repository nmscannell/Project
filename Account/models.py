from django.db import models

# Create your models here.


class Account(models.Model):
    accountName = models.CharField(max_length=20)
    accountEmail = models.EmailField()
    accountTitle = models.CharField(max_length=10, default="")
    accountHP = models.CharField(max_length=20, default="")
    accountAddress = models.CharField(max_length=3, default="")

    def __str__(self):
        return str("Name:" + self.accountName + "Email:" + self.accountEmail)

    def display(self):
        return str("Name:" + self.accountName + " Email:" + self.accountEmail + "\n"
                   +" Title:" + self.accountTitle + " HomePhone:" + self.accountHP
                   + "\n" + "Address:" + self.accountAddress)
