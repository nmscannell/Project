from django.test import TestCase
from Lab.CreateLab import CreateLab
from Course.models import Course
from Lab.models import Lab


class Test_CreateLab(TestCase):
    def setUp(self):
        self.CL = CreateLab()

        Course.objects.create(name="TemporalMechanics", number=784, onCampus=True, classDays="MW",
                              classHoursStart=1000, classHoursEnd=1100)

        Course.objects.create(name="WarpTheory", number=633, onCampus=False, classDays="TR", classHoursStart=1200,
                              classHoursEnd=1250)

        Course.objects.create(name="QuantumMechanics", number=709, onCampus=True, classDays="MWF",
                              classHoursStart=1030, classHoursEnd=1145)

        self.c1 = Course.objects.get(name="TemporalMechanics")
        self.c2 = Course.objects.get(name="WarpTheory")
        self.c3 = Course.objects.get(name="QuantumMechanics")

        Lab.objects.create(course=self.c1, sectionNumber=201, meetingDays="W", startTime=1000, endTime=1200)
        Lab.objects.create(course=self.c1, sectionNumber=202, meetingDays="F", startTime=1400, endTime=1700)
        Lab.objects.create(course=self.c1, sectionNumber=203, meetingDays="T", startTime=1000, endTime=1200)

        self.command_create_lab = ["createLab", "633", "201", "T", "1000", "1100"]
        self.command_create_lab_multiple_section = ["createLab", "633", "202", "W", "1300", "1400"]
        self.command_create_lab2 = ["createLab", "709", "201", "R", "1200", "1345"]

        self.command_section_exists = ["createLab", "358", "002", "MW", "1000", "1100"]
        self.command_create_lab_no_args = ["createLab"]
        self.command_create_lab_no_courseNumber = ["createLab", "001", "W", "1000", "1200"]
        self.command_create_lab_no_sectionNumber = ["createLab", "540", "W", "1000", "1200"]

    def test_lab_was_successfully_created(self):
        CreateLab.createLab(self.CL, self.command_create_lab)
        CreateLab.createLab(self.CL, self.command_create_lab_multiple_section)
        CreateLab.createLab(self.CL, self.command_create_lab2)

        a = Lab.objects.get(course=self.c2, sectionNumber=201)
        self.assertEqual(a.course, self.c2)
        self.assertEqual(a.sectionNumber, 201)
        self.assertEqual(a.meetingDays, "T")
        self.assertEqual(a.starTime, 1000)
        self.assertEqual(a.endTime, 1100)

        b = Lab.objects.get(course=self.c2, sectionNumber=202)
        self.assertEqual(b.course, self.c2)
        self.assertEqual(b.sectionNumber, 202)
        self.assertEqual(b.meetingDays, "M")
        self.assertEqual(b.starTime, 1300)
        self.assertEqual(b.endTime, 1400)

        c = Lab.objects.get(course=self.c3, sectionNumber=201)
        self.assertEqual(c.course, self.c3)
        self.assertEqual(c.sectionNumber, 201)
        self.assertEqual(c.meetingDays, "T")
        self.assertEqual(c.starTime, 1200)
        self.assertEqual(c.endTime, 1345)




#    def test_section_was_already_existed(self):
#        self.assertEqual((CreateLab.createLab(self.CL, self.command_section_exists)),
#                         "Course already exists")

#    def test_lab_no_argument(self):
#        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_no_args))

#    def test_lab_no_courseNumber(self):
#        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_no_courseNumber))

#    def test_lab_no_sectionNumber(self):
#        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_no_sectionNumber))