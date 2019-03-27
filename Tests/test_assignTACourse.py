import unittest
from Commands import assignTACourse
from Course import Course
from teachingAssistant import teachingAssistant

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.TA1 = teachingAssistant()
        self.Course1 = Course(361)
        self.Course2 = Course(250)

    def test_assignTACourse(self):
        self.assertEqual(len(self.TA1.courses), 0)

        assignTACourse.assignTACourse(self.TA1, self.Course1)

        self.assertEqual(len(self.TA1.courses), 1)
        self.assertEqual(self.TA1.courses[0], 361)

        assignTACourse.assignTACourse(self.TA1, self.Course1)

        self.assertEqual(len(self.TA1.courses), 2)
        self.assertEqual(self.TA1.courses[0], 361)
        self.assertEqual(self.TA1.courses[1], 250)

    def test_setStatus(self):
        self.assertFalse(self.TA1.graderStatus)

        assignTACourse.setStatus(self.TA1, False)

        self.assertFalse(self.TA1.graderStatus)

        assignTACourse.setStatus(self.TA1, True)

        self.assertTrue(self.TA1.graderStatus)

        assignTACourse.setStatus(self.TA1, True)

        self.assertTrue(self.TA1.graderStatus)
        
if __name__ == '__main__':
    unittest.main()
