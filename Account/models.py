from django.db import models

# Create your models here.


class Account(models.Model):
    Name = models.CharField(max_length=20)
    password = models.CharField(max_length=20, default="password")
    title = models.IntegerField(default=0)
    currentUser = models.BooleanField(default=False)

    def __str__(self):
        return self.Name



