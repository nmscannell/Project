import unittest
from Commands import createAccount
from instructor import instructor
from Directory import Directory


class MyTestCase(unittest.TestCase):
    def setUp(self):
        self.Instructor1 = instructor("Bob")
        self.Directory = Directory()
        self.Directory.data.append(self.Instructor1)
        self.Directory.manyItems = 1

    def test_createAccount(self):
        #should not be able to create an account that is all ready in the directory
        with self.assertRaises(ValueError):
            createAccount.createAccount("Bob", self.Directory)

        createAccount("Joe", self.Directory)

        self.assertEqual(self.Directory.manyItems, 2)
        self.assertEqual(self.Directory.data[1], "Joe")
        self.assertEqual(self.Directory.data[0], "Bob")


if __name__ == '__main__':
    unittest.main()
