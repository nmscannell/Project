from django.db import models
from Course.models import Course

# Create your models here.


class InstructorCourse(models.Model):
    course = models.ForeignKey(Course, default=None, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course)