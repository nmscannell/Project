from django.test import TestCase
from Course.models import Course
from Lab.models import Lab
from Account.models import Account
from TaLab.AssignTaLab import AssignTaLab
from TaLab.models import TaLab


class TestAssignTaLab(TestCase):

    def setUp(self):
        Account.objects.create(userName='hsimpson', title='1')
        Course.objects.create(number='361')
        Course.objects.create(number='351')
        self.Course1 = Course.objects.get(number='361')
        self.Course2 = Course.objects.get(number='351')
        Lab.objects.create(sectionNumber=804, course=self.Course1)
        Lab.objects.create(sectionNumber=803, course=self.Course2)
        Lab.objects.create(sectionNumber=804, course=self.Course2)
        self.atl = AssignTaLab()

    def test_assignTaLab_accountNotFound(self):
        self.assertEqual(self.atl.assignTaLab(["assigntalab", "what", "361", "804"]), "Invalid account name")

        self.assertFalse(TaLab.objects.exists())

    def test_assignTaLab_courseNotFound(self):
        self.assertEqual(self.atl.assignTaLab(["assigntalab", "hsimpson", "111", "804"]), "Invalid course number")

        self.assertFalse(TaLab.objects.exists())

    def test_assignTaLab_labNotFound(self):
        self.assertEqual(self.atl.assignTaLab(["assigntalab", "hsimpson", "361", "444"]), "Invalid lab section")

        self.assertFalse(TaLab.objects.exists())

    def test_assignTaLab_labNotCourse(self):
        self.assertEqual(self.atl.assignTaLab(["assigntalab", "hsimpson", "361", "803"]), "Invalid lab section")

        self.assertFalse(TaLab.objects.exists())

    def test_assignTaLab_success(self):
        self.assertEqual(self.atl.assignTaLab(["assigntalab", 'hsimpson', "361", "804"]), "TA successfully assigned")

        self.assertTrue(TaLab.objects.exists())

        a = TaLab.objects.get()

        self.assertEqual(a.Lab, Lab.objects.get(sectionNumber=804, course=Course.objects.get(number=361)))

        self.assertEqual(a.TA, Account.objects.get(userName='hsimpson'))


