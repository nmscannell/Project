from unittest import TestCase
from Directory import Directory
from account import account
from teachingAssistant import  teachingAssistant
from instructor import  instructor

class TestDirectory(TestCase):

    def setUp(self):
        self.Directory1 = Directory()
        self.Directory2 = Directory()
        self.account1 = instructor("firstAccount")
        self.account2 = teachingAssistant("secondAccount")
        self.account3 = instructor("lastAccount")
        self.Directory2.data.append(self.account1)
        self.Directory2.data.append(self.account2)
        self.Directory2.data.append(self.account3)
        self.Directory2.manyItems = 3

    def test_insert(self):
        self.assertEqual(len(self.Directory1.data), 0)
        self.assertEqual(self.Directory1.manyItems, 0)

        self.Directory1.insert(self.account1)

        self.assertEqual(self.Directory1.data[0], self.account1)
        self.assertEqual(self.Directory1.manyItems, 1)

        self.Directory1.insert(self.account2)

        self.assertEqual(self.Directory1.data[1], self.account2)
        self.assertEqual(self.Directory1.manyItems, 2)
        self.assertEqual(self.Directory1.data[0], self.account1)

        self.Directory1.insert(self.account3)

        self.assertEqual(self.Directory1.data[2], self.account3)
        self.assertEqual(self.Directory1.manyItems, 3)
        self.assertEqual(self.Directory1.data[0], self.account1)
        self.assertEqual(self.Directory1.data[1], self.account2)

        #Should not be able to insert an account that already exists
        with self.assertRaises(ValueError):
            self.Directory1.insert(self.account1)

    def test_remove(self):
        self.assertEqual(len(self.Directory2.data), 3)
        self.assertEqual(self.Directory2.manyItems, 3)
        self.assertEqual(self.Directory2.data[1], "secondAccount")

        self.Directory2.remove("secondAccount")

        self.assertEqual(self.Directory2.manyItems, 2)
        self.assertEqual(self.Directory2.data[0], "firstAccount")
        self.assertEqual(self.Directory2.data[1], "lastAccount")

        self.Directory2.remove("firstAccount")

        self.assertEqual(self.Directory2.manyItems, 1)
        self.assertEqual(self.Directory2.data[0], "lastAccount")

        self.Directory2.remove("lastAccount")

        self.assertEqual(self.Directory2.manyItems, 0)
        self.assertEqual(len(self.Directory2.data), 0)

        #Should raise and exception if remove is called on something that isnt in the directory
        with self.assertRaises(ValueError):
            self.Directory2.remove("firstAccount")

    def test_isEmpty(self):
        self.assertTrue(self.Directory1.isEmpty())
        self.assertFalse(self.Directory2.isEmpty())

    def test_getAccount(self):
        #should not be able to get an account that doesn't exist
        with self.assertRaises(ValueError):
            self.account4 = self.Directory1.getAccount("firstAccount")

        self.assertEqual(self.Directory2.manyItems, 3)

        self.account4 = self.Directory2.getAccount("firstAccount")

        self.assertEqual(self.account4, self.account1)

        self.assertEqual(self.Directory2.manyItems, 3)

    def test_size(self):
        self.assertEqual(self.Directory1.size(), 0)
        self.assertEqual(self.Directory2.size(), 3)
