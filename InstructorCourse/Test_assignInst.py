from django.test import TestCase
from InstructorCourse.assignInst import assignInst
from InstructorCourse.models import InstructorCourse
from main import models
from Course.models import Course
from Account.models import Account


class TestAssignInst(TestCase):

    def setUp(self):
        self.AI = assignInst()
        Course.objects.create(number="535")
        Course.objects.create(number="317")
        self.course1 = Course.objects.get(number="535")
        self.course2 = Course.objects.get(number="317")
        Account.objects.create(userName="cheng41", title="2")

    def test_assignInst_successfully_created(self):

        self.assertEqual(self.AI.assignInst(["assigninstructorcourse", "535", "cheng41"]),
                         "Instructor was successfully assigned to class")
        self.assertTrue(InstructorCourse.objects.exists())
        a=InstructorCourse.objects.get()
        self.assertEqual(a.course, Course.objects.get(number="535"))
        self.assertEqual(a.course, Course.objects.get(number="317"))
        self.assertEqual(a.instructor, Account.objects.get(userName="cheng41"))

    def test_assignInst_course_already_existed(self):
        self.assertEqual((self.AI.assignInst(["assigninstructorcourse", "351", "boyland52"])),
                         "Course already exists")

    def test_assignInst_no_argument(self):
        self.assertEqual((self.AI.assignInst(["assigninstructorcourse"])),
                         "Please, type the command in the following format assigninstructorcourse classNumber username")

    def test_assignInst_no_courseNumber(self):
        self.assertEqual((self.AI.assignInst(["assigninstructorcourse", "bob824"])),
                         "Please, type the course number")

    def test_assignInst_no_username(self):
        self.assertEqual((self.AI.assignInst(["assigninstructorcourse", "595"])),
                         "Please, type your user name")


