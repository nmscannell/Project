from django.test import TestCase
from Course.models import Course
from Lab.models import Lab
from Account.models import Account
from TaLab.AssignTaLab import AssignTaLab


class TestAssignTaLab(TestCase):

    def setUp(self):
        Account.objects.create(userName='hsimpson', title='1')
        Course.objects.create(number='361')
        self.Course = Course.objects.get(number='361')
        Lab.objects.create(sectionNumber=804, course=self.Course)
        self.atl = AssignTaLab()

    def test_assignTaLab_accountNotFound(self):
        self.assertEqual(self.atl.assignTaLab(["assigntalab", "what", "361", "804"]), "Invalid account name")

    def test_assignTaLab_courseNotFound(self):
        self.assertEqual(self.atl.assignTaLab(["assigntalab", "hsimpson", "111", "804"]), "Invalid course number")

    def test_assignTaLab_labNotFound(self):
        self.assertEqual(self.atl.assignTaLab(["assigntalab", "hsimpson", "361", "444"]), "Invalid lab section")




