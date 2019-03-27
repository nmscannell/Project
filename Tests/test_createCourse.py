from unittest import TestCase
from Commands import createCourse
from CourseCatalog import CourseCatalog

class test_createCourse(TestCase):

    def setUp(self):
        self.Course1 = createCourse.createCourse(self, "Data Structures", 351, "TR", "9:00", "9:50")

    def test_name_assignment(self):
        self.assertEqual(self.Course1.getName(), "Data Structures")

    def test_number_assignment(self):
        self.assertEqual(self.Course1.getNumber(), 351)

    def test_meeting_days_assignment(self):
        self.assertEqual(self.Course1.getMeetingDays(), "TR")

    def test_start_time_assignment(self):
        self.assertEqual(self.Course1.getStartTime(), "9:00")

    def test_end_time_assignment(self):
        self.assertEqual(self.Course1.getEndTime(), "9:50")

    def test_added_to_catalog(self):
        self.assertTrue(self.Course1 in CourseCatalog.data)













if __name__ == '__main__':
    unittest.main()
