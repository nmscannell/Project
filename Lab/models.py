from django.db import models

# Create your models here.

class CreateLab(models.Model):
    courseNumber = models.IntegerField(max_length = 5, default= 0)
    sectionNumber = models.CharField(max_length = 3, default= 0)
    meetingDays = models.CharField(max_length= 10, default=" ")
    startTime = models.IntegerField(max_length= 10, default="00:00")
    endTime = models.IntegerField(max_length= 10, default="00:00")



