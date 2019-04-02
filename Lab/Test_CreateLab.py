from django.test import TestCase
from Lab.CreateLab import CreateLab
from Lab.models import models


class Test_CreateLab(TestCase):

    def setUp(self):
        CreateLab.objects.create(courseNumber="52312", sectionNumber="001",
                              meetingDays="W", startTime="10:00", endTime="12:00")
        CreateLab.objects.create(courseNumber="52312", sectionNumber="002",
                                 meetingDays="F", startTime="14:00", endTime="17:00")
        CreateLab.objects.create(courseNumber="54911", sectionNumber="001",
                                 meetingDays="M,W", startTime="10:00", endTime="12:00")

    def test_(self):
        pass
    def test_(self):
        pass
