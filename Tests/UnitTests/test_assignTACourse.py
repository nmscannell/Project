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
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "Neelix", "535"]), "Invalid TA username.")

        self.assertFalse(TACourse.objects.exists())

    def test_assignTACourse_courseNotFound(self):
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "Tuvix", "874"]), "Invalid course number.")

        self.assertFalse(TACourse.objects.exists())

    def test_assignTACourse_success(self):
        self.assertEqual(self.assign.assignTACourse(["assigntacourse", "Tuvix", "535"]), "Assignment successful.")

        self.assertTrue(TACourse.objects.exists())

        a = TACourse.objects.get()

        self.assertEqual(a.Course, Course.objects.get(number=535))

        self.assertEqual(a.TA, Account.objects.get(userName="Tuvix"))


