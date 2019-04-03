from django.test import TestCase
from Lab.CreateLab import CreateLab
from Lab.models import Lab
from main import models


class Test_CreateLab(TestCase):

    def setUp(self):
        self.CL = CreateLab()
        CreateLab.objects.create(courseNumber=52312, sectionNumber="001",
                                 meetingDays="W", startTime="1000", endTime="1200")
        CreateLab.objects.create(courseNumber=52312, sectionNumber="002",
                                 meetingDays="F", startTime="1400", endTime="1700")
        CreateLab.objects.create(courseNumber=54911, sectionNumber="003",
                                 meetingDays="M,W", startTime="10:00", endTime="12:00")

    def test_lab_was_successfully_created(self):
        a = CreateLab.createLab().get(courseNumber=52312, sectionNumber="001")
        self.assertEqual(a.meetingDays, "W")
        self.assertEqual(a.starTime, "1000")
        self.assertEqual(a.endTime, "1200")
        b = CreateLab.createLab().get(courseNumber=52312, sectionNumber="002")
        self.assertEqual(b.meetingDays, "F")
        self.assertEqual(b.starTime, "1400")
        self.assertEqual(b.endTime, "1700")
        c = CreateLab.createLab().get(courseNumber=54911, sectionNumber="001")
        self.assertEqual(c.meetingDays, "M W")
        self.assertEqual(c.starTime, "1000")
        self.assertEqual(c.endTime, "1200")

    def test_lab_was_already_existed(self):
            with self.assertRaises(SystemError):
                self.models.command("createLab 52312 '001' 'w' '1000' '1200' ")

    def test_lab_no_argument(self):
        self.assertEqual(models.command, "createLab")

    def test_lab_no_courseNumber(self):
        self.assertEqual(models.command, "createLab '001' 'w' '1000' '1200' ")

    def test_lab_no_sectionNumber(self):
        self.assertEqual(models.command, "createLab 52312 'w' '1000' '1200' ")






