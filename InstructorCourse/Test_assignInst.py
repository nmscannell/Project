from django.test import TestCase
from InstructorCourse.assignInst import assignInst
from InstructorCourse.models import InstructorCourse
from main import models


class Test_assignInst(TestCase):

    def setUp(self):
        self.AI = assignInst()
        InstructorCourse.objects.create(classNumber=52312, userName="django123")
        InstructorCourse.objects.create(classNumber=52312, username="stack_over_flow")
        InstructorCourse.objects.create(courseNumber=54911, userName="potato24")
        self.command_assign_course = ["assignInst", "42133", "jack2131"]
        self.command_section_was_already_existed = ["assignInst", "12451", "super999"]
        self.command_assignment_no_args = ["assignInst"]
        self.command_assignment_no_courseNumber = ["assignInst", "pycharm591"]
        self.command_assignment_no_userName = ["assignInst", "58123"]

    def test_assignment_was_successfully_created(self):
        assignInst.assignInst(self.AI, self.command_assign_course)
        a = InstructorCourse.objects.get(username="system928down")



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






