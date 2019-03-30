from django.db import models

# Create your models here.


class Course(models.Model):
    name = models.CharField(max_length=20, default=" ")
    number = models.IntegerField(default=000)
    onCampus = models.BooleanField(default=True)
    classDays = models.CharField(max_length=10, default=" ")
    classHoursStart = models.CharField(max_length=10, default="00:00")
    classHoursEnd = models.CharField(max_length=10, default="00:00")

    def __str__(self):
        return None
