from unittest import TestCase
from Commands import createLab
from Course import Course

class test_createLab(TestCase):

    def setUp(self):
        self.Course1 = Course(361)
        self.Lab1 = createLab.createLab(self, 361, 101, "W", 1300, 1445 )

    def test_lab_assigned_to_course(self):
        self.assertTrue(self.Lab1 in self.Course1.courseInfo["labs"])

    def test_lab_section_assigned(self):
        self.assertEqual(self.Lab1.sectionNumber, 101)


