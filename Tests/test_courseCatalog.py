from unittest import TestCase
from CourseCatalog import CourseCatalog


class TestCourseCatalog(TestCase):

    def setUp(self):
        self.CourseCatalog1 = CourseCatalog()
        self.CourseCatalog2 = CourseCatalog()
        self.CourseCatalog2.manyItems = 3
        self.CourseCatalog2.data.append(361)
        self.CourseCatalog2.data.append(101)
        self.CourseCatalog2.data.append(102)

    def test_insert(self):
        self.assertEqual(self.CourseCatalog1.manyItems, 0)
        self.assertEqual(len(self.CourseCatalog1.data), 0)

        self.CourseCatalog1.insert(361)

        self.assertEqual(self.CourseCatalog1.manyItems, 1)
        self.assertEqual(self.CourseCatalog1.data[0], 361)

        self.CourseCatalog1.insert(101)

        self.assertEqual(self.CourseCatalog1.manyItems, 2)
        self.assertEqual(self.CourseCatalog1.data[0], 361)
        self.assertEqual(self.CourseCatalog1.data[1], 101)

        self.CourseCatalog1.insert(102)

        self.assertEqual(self.CourseCatalog1.manyItems, 3)
        self.assertEqual(self.CourseCatalog1.data[0], 361)
        self.assertEqual(self.CourseCatalog1.data[1], 101)
        self.assertEqual(self.CourseCatalog1.data[2], 102)

        #Value error should be raised when trying to add a course that already exists in the catalog
        with self.assertRaises(ValueError):
            self.CourseCatalog1.insert(361)
            self.CourseCatalog1.insert(101)
            self.CourseCatalog1.insert(102)

    def test_remove(self):
        self.assertEqual(self.CourseCatalog2.manyItems, 3)
        self.assertEqual(self.CourseCatalog2.data[0], 361)
        self.assertEqual(self.CourseCatalog2.data[1], 101)
        self.assertEqual(self.CourseCatalog2.data[2], 102)

        #Should raise a value error when remove is called on a course not in the catalog
        with self.assertRaises(ValueError):
            self.assertEqual(self.CourseCatalog2.remove(233))

        self.CourseCatalog2.remove(101)

        self.assertEqual(self.CourseCatalog2.manyItems, 2)
        self.assertEqual(self.CourseCatalog2.data[0], 361)
        self.assertEqual(self.CourseCatalog2.data[1], 102)

        self.CourseCatalog2.remove(361)

        self.assertEqual(self.CourseCatalog2.manyItems, 1)
        self.assertEqual(self.CourseCatalog2.data[0], 102)

        self.CourseCatalog2.remove(102)

        self.assertEqual(self.CourseCatalog2.manyItems, 0)
        self.assertEqual(len(self.CourseCatalog2.data), 0)

    def test_isEmpty(self):
        self.assertTrue(self.CourseCatalog1.isEmpty())
        self.assertFalse(self.CourseCatalog2.isEmpty())

    def test_getCourse(self):
        #Should raise an error if you try to get a course that is not in the catalog
        with self.assertRaises(ValueError):
            self.CourseCatalog2.getCourse(233)

        self.Course1 = self.CourseCatalog2.getCourse(102)

        self.assertEqual(self.Course1.courseName, 102)

        self.assertEqual(self.CourseCatalog2.manyItems, 3)

    def test_size(self):
        self.assertEqual(self.CourseCatalog1.size(), 0)
        self.assertEqual(self.CourseCatalog2.size(), 3)
