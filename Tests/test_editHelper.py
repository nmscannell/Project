from unittest import TestCase
from editHelper import EditHelper
from account import account

class TestEditHelper(TestCase):

    def setUp(self):
        self.Account1 = account()
        self.Account1.accountName = "Mr.Sparkle"
        self.Account1.accountInfo["Home Phone"] = "555-0113"
        self.Account1.accountInfo["Email"] = "chunkylover53@aol.com"
        self.Account1.accountInfo["address"] = "123 Fake Street"
        self.Account1.accountInfo["Office Phone"] = "555-5555"
        self.Account1.accountInfo["Office hours"] = "All day everyday"

    def test_updateHPhone(self):
        self.EditHelper.updateHPhone("Mr. Sparkle", "514-4864")
        self.assertEqual(self.Account1.getInfo("Home Phone"), "514-4864")

    def test_updateOPhone(self):
        self.EditHelper.updateOPhone("Mr. Sparkle", "457-5321")
        self.assertEqual(self.Account1.getInfo("Office Phone"), "457-5321")

    def test_updateEmail(self):
        self.EditHelper.updateEmail("Mr. Sparkle", "sparks@yahoo.com")
        self.assertEqual(self.Account1.getInfo("Email"), "sparks@yahoo.com")

    def test_updateAddress(self):
        self.EditHelper.updateAddress("Mr. Sparkle", "4837 W Drury Ln")
        self.assertEqual(self.Account1.getInfo("Address"), "4837 W Drury Ln")

    def test_updateOHours(self):
        self.EditHelper.updateOHours("Mr. Sparkle", "10:00 - 11:00 AM TR")
        self.assertEqual(self.Account1.getInfo("Office hours"), "10:00 - 11:00 AM TR")
