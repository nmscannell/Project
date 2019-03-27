from unittest import TestCase
from Course import Course

class TestCourse(TestCase):

    def setUp(self):
        self.Course1 = Course()
        self.Course2 = Course()
        self.Course2.courseNumber = 361
        self.Course2.courseInfo["meetingDays"] = "Tuesday Thursday"
        self.Course2.courseInfo["meetingTime"] = "10:00 - 10:50"

    def test_getNumber(self):
        self.assertEqual(self.Course1.getNumber(), 1)
        self.assertEqual(self.Course2.getNumber(), 361)

    def test_setNumber(self):
        self.Course1.setNumber(250)

        self.assertEqual(self.Course1.courseNumber, 250)

        #Should be less than 1000 and grater than 0
        with self.assertRaises(ValueError):
            self.Course1.setNumber(0)
            self.Course1.setNumber(-1)
            self.Course1.setNumber(1000)

    def test_getCourseInfo(self):
        #Should raise an exception if getCourseInfo is called on a field that does not exist in the dictionary
        with self.assertRaises(ValueError):
            self.Course1.getCourseInfo("courseDifficulty")

        self.assertEqual(self.Course2.getCourseInfo("meetingTime"), "10:00 - 10:50")
        self.assertEqual(self.Course2.getCourseInfo("meetingDays"), "Tuesday Thursday")

    def test_setCourseInfo(self):
        #Should raise an exception in setCourse Info is called to change a field no in the dictionary
        with self.assertRaises(ValueError):
            self.Course1.setCourseInfo("courseDifficulty", "Nightmare")

        self.Course1.setCourseInfo("meetingTime", "10:00 - 10:01")

        self.assertEqual(self.Course1.courseInfo["meetingTime"], "10:00 - 10:01")

        self.Course1.courseInfo("meetingDays", "Tuesday Thursday")

        self.assertEqual(self.Course1.courseInfo["meetingDays"], "Tuesday Thursday")
