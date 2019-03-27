from unittest import TestCase
from account import account


class TestAccount(TestCase):

    def setUp(self):
        self.Account1 = account()
        self.Account1.accountName = "Mr.Sparkle"
        self.Account1.accountInfo["Home Phone"] = "555-0113"
        self.Account1.accountInfo["Email"] = "chunkylover53@aol.com"
        self.Account1.accountInfo["address"] = "123 Fake Street"
        self.Account1.accountInfo["Office Phone"] = "555-5555"
        self.Account1.accountInfo["Office hours"] = "All day everyday"


    def test_viewPersonal(self):
        self.assertEqual(self.Account1.viewName(),"Mr.Sparkle")
        self.assertEqual(self.Account1.viewHomePhone(), "Not public info")
        self.assertEqual(self.Account1.viewOfficePhone(), "555-5555")
        self.assertEqual(self.Account1.viewAdress(), "Not public info")
        self.assertEqual(self.Account1.viewEmail(), "chunkylover53@alo.com")
        self.assertEqual(self.Account1.viewOfficeHours, "All day everyday")
