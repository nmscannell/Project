import unittest
from Course import Course
from Lab import Lab
from teachingAssistant import teachingAssistant

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.Course1 = Course(361)
        self.TA1 = teachingAssistant()
        self.TA2 = teachingAssistant()
        self.TA3 = teachingAssistant()
        self.Lab1 = Lab(361,601)
        self.Lab2 = Lab(361,602)
        self.Lab3=  Lab(361,603)
        self.Lab4 = Lab(361,604)
        self.Lab5 = Lab(361,605)
        self.assignTALab.assignTALab(self.TA1, self.Lab1)
        self.assignTALab.assignTALab(self.TA2, self.Lab2)
        self.assignTALab.assignTALab(self.TA3, self.Lab3)
        self.assignTALab.assignTALab(self.TA1, self.Lab4)
        self.assignTALab.assignTALab(self.TA3, self.Lab5)

    def test_LabAssignments(self):
        self.assertEqual(self.Lab1.assigned, TA1)
        self.assertEqual(self.Lab2.assigned, TA2)
        self.assertEqual(self.Lab3.assigned, TA3)
        self.assertEqual(self.Lab4.assigned, TA1)
        self.assertEqual(self.Lab5.assigned, TA3)
        self.assignTALab.assignTALab(self.TA2, self.Lab5)
        self.assertEqual(self.Lab5.assigned, TA2)


if __name__ == '__main__':
    unittest.main()


