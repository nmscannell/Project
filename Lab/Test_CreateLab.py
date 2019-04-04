from django.test import TestCase
from Lab.CreateLab import CreateLab
from Lab.models import Lab
from main import models


class Test_CreateLab(TestCase):
    def setUp(self):
        self.CL = CreateLab()
        Lab.objects.create(courseNumber=52312, sectionNumber="001", meetingDays="W", startTime="1000", endTime="1200")
        Lab.objects.create(courseNumber=52312, sectionNumber="002", meetingDays="F", startTime="1400", endTime="1700")
        Lab.objects.create(courseNumber=54911, sectionNumber="003", meetingDays="MW", startTime="1000",
                           endTime="1200")
        self.command_create_lab = ["createLab", 42125, "001", "T", "1000", "1100"]
        self.command_section_was_already_existed = ["createLab", 23462, "002", "MW",
                                                    "1000", "1100"]
        self.command_create_lab_no_args = ["createLab"]
        self.command_create_lab_no_courseNumber = ["createLab", "001", "W", "1000", "1200"]
        self.command_create_lab_no_sectionNumber = ["createLab", 52312, "W", "1000", "1200"]

    def test_lab_was_successfully_created(self):
        CreateLab.createLab(self.CL, self.command_create_lab)
        a = Lab.objects.get(courseNumber=91231, sectionNumber="001")
        self.assertEqual(a.courseNumber, 91231)
        self.assertEqual(a.sectionNumber, "001")
        self.assertEqual(a.meetingDays, "TR")
        self.assertEqual(a.starTime, "1300")
        self.assertEqual(a.endTime, "1500")
        b = Lab.objects.get(courseNumber=19201, sectionNumber="001")
        self.assertEqual(b.courseNumber, 19201)
        self.assertEqual(b.sectionNumber, "001")
        self.assertEqual(b.meetingDays, "M")
        self.assertEqual(b.starTime, "1500")
        self.assertEqual(b.endTime, "1600")
        c = Lab.objects.get(courseNumber=51999, sectionNumber="004")
        self.assertEqual(c.courseNumber, 51999)
        self.assertEqual(c.sectionNumber, "004")
        self.assertEqual(c.meetingDays, "T")
        self.assertEqual(c.starTime, "1000")
        self.assertEqual(c.endTime, "1200")

    def test_section_was_already_existed(self):
        self.assertEqual((CreateLab.createLab(self.CL, self.command_section_was_already_existed)),
                         "Course already exists")

    def test_lab_no_argument(self):
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_no_args))

    def test_lab_no_courseNumber(self):
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_no_courseNumber))

    def test_lab_no_sectionNumber(self):
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_no_sectionNumber))






