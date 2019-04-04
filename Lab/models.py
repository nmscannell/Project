from django.db import models
from Course.models import Course
# Create your models here.


class Lab(models.Model):

    models.ForeignKey(Course, on_delete=models.CASCADE)
    sectionNumber = models.IntegerField(default=000)
    meetingDays = models.CharField(max_length=10, default=" ")
    startTime = models.IntegerField(default=0000)
    endTime = models.IntegerField(default=0000)

    def __str__(self):
        return None
