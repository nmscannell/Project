from django.test import TestCase
from Lab.CreateLab import CreateLab
from Lab.models import models



class Test_CreateLab(TestCase):

    def setUp(self):
        CreateLab.objects.create(courseNumber= 52312, sectionNumber="001",
                                 meetingDays="W", startTime="10:00", endTime="12:00")
        CreateLab.objects.create(courseNumber=52312, sectionNumber="002",
                                 meetingDays="F", startTime="14:00", endTime="17:00")
        CreateLab.objects.create(courseNumber=54911, sectionNumber="003",
                                 meetingDays="M,W", startTime="10:00", endTime="12:00")

    def test_lab_was_successfully_created(self):
        a = CreateLab.objects.get(courseNumber=52312, sectionNumber="001")
        self.assertEqual(a.meetingDays, "W")
        self.assertEqual(a.starTime, "10:00")
        self.assertEqual(a.endTime, "12:00")
        b = CreateLab.objects.get(courseNumber=52312, sectionNumber="002")
        self.assertEqual(b.meetingDays, "F")
        self.assertEqual(b.starTime, "14:00")
        self.assertEqual(b.endTime, "17:00")
        c = CreateLab.objects.get(courseNumber=54911, sectionNumber="001")
        self.assertEqual(c.meetingDays, "M,W")
        self.assertEqual(c.starTime, "10:00")
        self.assertEqual(c.endTime, "12:00")

    def test_lab_was_already_existed(self):
            with self.assertRaises(SystemError):
                self.models.command("createLab 52312 '001' 'w' '10:00' '12:00' ")


    def test_lab_no_argument(self):
        self.assertEqual(models.command, "createLab")
        



