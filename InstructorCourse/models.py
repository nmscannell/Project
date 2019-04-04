from django.db import models
from Course.models import Course

# Create your models here.


class InstructorCourse(models.Model):
    models.ManyToManyField(Course, on_delete=models.CASCADE)



    def __str__(self):
        return None
