from django.test import TestCase
from InstructorCourse.assignInst import assignInst
from InstructorCourse.models import InstructorCourse
from main import models


class Test_assignInst(TestCase):

    def setUp(self):
        self.AI = assignInst()
        InstructorCourse.objects.create(coursesNumber=52312, userName="django123")
        InstructorCourse.objects.create(courseNumber=52312, username="stack_over_flow")
        InstructorCourse.objects.create(courseNumber=54911, userName="potato24")
        self.command_assign_course = ["assignInst", "42133", "jack2131"]
        self.command_section_was_already_existed = ["assignInst", "12451", "super999"]
        self.command_assignment_no_args = ["assignInst"]
        self.command_assignment_no_courseNumber = ["assignInst", "pycharm591"]
        self.command_assignment_no_userName = ["assignInst", "58123"]

    def test_assignment_was_successfully_created(self):
        assignInst.assignInst(self.AI, self.command_assign_course)
        a = InstructorCourse.objects.get(userName="system928down")
        self.assertEqual(a.classNumber, 12425)
        self.assertEqual(a.userName, "system928down")
        b = InstructorCourse.objects.get(userName="default122")
        self.assertEqual(b.classNumber, 51221)
        self.assertEqual(b.userName, "default122")
        c = InstructorCourse.objects.get(userName="bucks213")
        self.assertEqual(b.classNumber, 12425)
        self.assertEqual(b.userName, "bucks213")

    def test_assignment_was_already_existed(self):
        self.assertEqual((assignInst.assignInst(self.AI, self.command_section_was_already_existed)),
                         "Course already exists")

    def test_lab_no_argument(self):
        self.assertEqual(assignInst.assignInst(self.AI, self.command_assignment_no_args))

    def test_lab_no_courseNumber(self):
        self.assertEqual(assignInst.assignInst(self.AI, self.command_assignment_no_courseNumber))

    def test_lab_no_sectionNumber(self):
        self.assertEqual(assignInst.assignInst(self.AI, self.command_assignment_no_userName))






