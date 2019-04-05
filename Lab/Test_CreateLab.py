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
        self.command_create_lab_multiple_section2 = ["createLab", "633", "203", "F", "1100", "1245"]
        self.command_create_lab2 = ["createLab", "709", "201", "R", "1200", "1345"]
        self.command_section_exists = ["createLab", "784", "201", "W", "1000", "1200"]
        self.command_create_lab_no_args = ["createLab"]
        self.command_create_lab_no_courseNumber = ["createLab", "001", "W", "1000", "1200"]
        self.command_create_lab_no_sectionNumber = ["createLab", "540", "W", "1000", "1200"]
        self.command_create_lab_no_daysOfWeek = ["createlab", "540", "001", "1000", "1200"]
        self.command_create_lab_noStartTime = ["createLab", "540", "001", "W", "1200"]
        self.command_create_lab_noEndTime = ["createLab", "540", "001", "W", "1000"]
        self.command_create_lab_courseDoesNotExist = ["createLab", "540", "001", "W", "1000", "1200"]

    def test_lab_was_successfully_created(self):
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab), "Lab successfully created")
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_multiple_section),
                         "Lab successfully created")
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab2), "Lab successfully created")
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_multiple_section2),
                         "Lab successfully created")

        a = Lab.objects.get(course=self.c2, sectionNumber=201)
        self.assertEqual(a.course, self.c2)
        self.assertEqual(a.sectionNumber, 201)
        self.assertEqual(a.meetingDays, "T")
        self.assertEqual(a.startTime, 1000)
        self.assertEqual(a.endTime, 1100)

        b = Lab.objects.get(course=self.c2, sectionNumber=202)
        self.assertEqual(b.course, self.c2)
        self.assertEqual(b.sectionNumber, 202)
        self.assertEqual(b.meetingDays, "W")
        self.assertEqual(b.startTime, 1300)
        self.assertEqual(b.endTime, 1400)

        c = Lab.objects.get(course=self.c3, sectionNumber=201)
        self.assertEqual(c.course, self.c3)
        self.assertEqual(c.sectionNumber, 201)
        self.assertEqual(c.meetingDays, "R")
        self.assertEqual(c.startTime, 1200)
        self.assertEqual(c.endTime, 1345)

        d = Lab.objects.get(course=self.c2, sectionNumber=203)
        self.assertEqual(d.course, self.c2)
        self.assertEqual(d.sectionNumber, 203)
        self.assertEqual(d.meetingDays, "F")
        self.assertEqual(d.startTime, 1100)
        self.assertEqual(d.endTime, 1245)

    def test_section_already_exists(self):
        self.assertEqual((CreateLab.createLab(self.CL, self.command_section_exists)),
                         "Lab already exists, lab not added")

    def test_lab_missing_arguments(self):
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_no_args),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_no_courseNumber),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_no_daysOfWeek),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_no_sectionNumber),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_noStartTime),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_noEndTime),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime")

    def test_courseDoesNotExist(self):
        self.assertEqual(CreateLab.createLab(self.CL, self.command_create_lab_courseDoesNotExist),
                         "The Course you are trying to create a lab for does not exist")