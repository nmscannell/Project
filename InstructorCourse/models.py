from django.db import models

# Create your models here.


class InstructorCourse(models.Model):
    classNumber = models.IntegerField(default=0)
    userName = models.CharField(max_length=20, default=" ")



    def __str__(self):
        return None