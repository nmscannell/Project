from django.test import TestCase
from Course.CreateCourse import CreateCourse
from Course.models import Course
from main import models

class Test_CreateCourse(TestCase):
    def setUp(self):
        Course.objects.create()
        Course.objects.create()