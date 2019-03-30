from django.db import models

# Create your models here.


class Lab(models.Model):
    courseNumber = models.IntegerField(default=00000)
    sectionNumber = models.IntegerField(default=000)
    meetingDays = models.CharField(max_length=10, default=" ")
    startTime = models.CharField(max_length=10, default="00:00")
    endTime = models.CharField(max_length=10, default="00:00")
