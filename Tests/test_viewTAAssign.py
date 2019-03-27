import unittest
from Commands import viewTAAssign
from teachingAssistant import teachingAssistant
from instructor import instructor

class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.TA = teachingAssistant()
        self.TA.courses.append(361)
        self.TA.labs.append(803)
        self.Instructor = instructor()

    def test_viewTAAssign(self):
        #should raise an error if you try and view a non TAs assignments
        with self.assertRaises(ValueError):
            viewTAAssign.viewTAAssign(self.Instructor)

        self.assertEqual(viewTAAssign.viewTAAssign(self.TA), "361 803")


if __name__ == '__main__':
    unittest.main()
