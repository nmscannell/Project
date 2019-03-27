import unittest
from editHelper import EditHelper


class TestEdit(unittest.TestCase):
    def testNSU(self):
        self.assertEqual(self.edit("user", "command", "arg"), "No such user.")

    def testEditHPhone(self):
        self.assertEqual(self.edit("user", "HPhone", "pho numb"), "Home phone number updated.")

    def testEditOPhone(self):
        self.assertEqual(self.edit("user", "OPhone", "pho numb"), "Office phone number updated.")

    def testEditOHours(self):
        self.assertEqual(self.edit("user", "OHours", "hrs"), "Office hours updated.")

    def testEditEmail(self):
        self.assertEqual(self.edit("user", "Email", "email"), "Email updated.")

    def testEditAddreess(self):
        self.assertEqual(self.edit("user", "Address", "address"), "Address updated.")


if __name__ == '__main__':
    unittest.main()
