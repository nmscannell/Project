from django.db import models

# Create your models here.


class Lab(models.Model):
    courseNumber = models.IntegerField(default=000)
    sectionNumber = models.CharField(max_length=10, default="000")
    meetingDays = models.CharField(max_length=10, default=" ")
    startTime = models.CharField(max_length=10, default="0000")
    endTime = models.CharField(max_length=10, default="0000")

    def __str__(self):
        return None
