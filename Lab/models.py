from django.db import models

# Create your models here.


class Lab(models.Model):

    courseNumber = models.IntegerField(default=000)
    sectionNumber = models.IntegerField(max_length=10, default=000)
    meetingDays = models.CharField(max_length=10, default=" ")
    startTime = models.IntegerField(default=0000)
    endTime = models.IntegerField(default=0000)

    def __str__(self):
        return None
