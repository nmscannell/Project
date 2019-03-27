from unittest import TestCase
from Lab import Lab


class TestLab(TestCase):

    def setUp(self):
        self.Lab1 = Lab()
        self.Lab2 = Lab()
        self.Lab2.sectionNumber = 803

    def test_getSection(self):
        self.assertEqual(self.lab2.getSection, 803)

    def test_setSection(self):
        #secition number should be greater than 800 and less than 810
        with self.assertRaises(ValueError):
            self.Lab1.setSection(800)
            self.Lab1.setSection(810)

        self.Lab1.setSection(804)
        self.assertEqual(self.Lab1.sectionNumber, 804)
