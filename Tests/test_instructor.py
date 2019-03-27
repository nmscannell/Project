from unittest import TestCase
from instructor import instructor


class TestInstructor(TestCase):

    def setUp(self):
        self.instructor1 = instructor()

    def test_addCouse(self):
        self.assertEqual(len(self.instructor1.courses), 0)
        self.instructor1.addcourse("CPS361")
        self.assertEqual(len(self.instructor1.courses), 1)
        self.instructor1.addcourse("CPS101")
        self.assertEqual(len(self.instructor1.courses), 2)


