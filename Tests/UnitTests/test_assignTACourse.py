from django.test import TestCase
from Course.models import Course
from Account.models import Account
from TACourse.AssignTACourse import AssignTACourse
from TACourse.models import TACourse


class TestAssignTACourse(TestCase):

    def setUp(self):
        Account.objects.create(userName="Tuvix", title="1")
        Course.objects.create(number="535")
        Course.objects.create(number="351")
        self.Course1 = Course.objects.get(number="535")
        self.Course2 = Course.objects.get(number="351")
        self.assign = AssignTACourse()

    def test_assignTACourse_accountNotFound(self):
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "Neelix", "351"]), "Invalid TA username.")

        self.assertFalse(TACourse.objects.exists())

    def test_assignTACourse_courseNotFound(self):
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "tuvix", "874"]), "Invalid course number")

        self.assertFalse(TACourse.objects.exists())

    def test_assignTACourse_success(self):
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "tuvix", "361"]), "Assignment successful")

        self.assertTrue(TaLab.objects.exists())

        a = TaLab.objects.get()

        self.assertEqual(a.Lab, Lab.objects.get(sectionNumber=804, course=Course.objects.get(number=361)))

        self.assertEqual(a.TA, Account.objects.get(userName='hsimpson'))


