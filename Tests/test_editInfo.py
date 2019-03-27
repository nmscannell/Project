import unittest


class TestEditInfo(unittest.TestCase):

    def testEditHPhone(self):
        self.assertEqual(self.editInfo("HPhone", "pho numb"), "Home phone number updated.")

    def testEditOPhone(self):
        self.assertEqual(self.editInfo("OPhone", "pho numb"), "Office phone number updated.")

    def testEditOHours(self):
        self.assertEqual(self.editInfo("OHours", "hrs"), "Office hours updated.")

    def testEditEmail(self):
        self.assertEqual(self.editInfo("Email", "email"), "Email updated.")

    def testEditAddreess(self):
        self.assertEqual(self.editInfo("Address", "address"), "Address updated.")


if __name__ == '__main__':
    unittest.main()
