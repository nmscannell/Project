import unittest
from Commands import viewCourseAssign
from instructor import instructor


class test_ViewCourseAssign(unittest.TestCase):

    def setUp(self):
        self.view = viewCourseAssign.viewCourseAssign()

    def test_instructor_can_view(self):
        self.assertEqual(self.view, instructor.displayAssignments())


if __name__ == '__main__':
    unittest.main()
