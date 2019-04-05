from django.db import models
from Course.models import Course
from Account.models import Account

# Create your models here.


class InstructorCourse(models.Model):
    instructor = models.ForeignKey(Account, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.instructor) + str(self.course)
