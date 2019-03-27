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


    def test_getName(self):
        self.assertEqual(self.Account1.getName(), "Mr.Sparkle")

    def test_setName(self):
        self.assertEqual(self.Account1.accountName, "Mr.Sparkle")
        self.Account1.setName("Homer")
        self.assertEqual(self.Account1.accountName, "Homer")

    def test_setInfo(self):
        #test changing the address
        self.assertEqual(self.Account1.accountInfo["address"], "123 Fake Street")
        self.Account1.setInfo("address", "742 Evergreen Terrace")
        self.assertEqual(self.Account1.accountInfo["address"], "742 Evergreen Terrace")

        #test changing the home phone
        self.assertEqual(self.Account1.accountInfo["Home Phone"], "555-0113")
        self.Account1.setInfo("Home Phone", "867-5309")
        self.assertEqual(self.Account1.accountInfo["Home Phone"], "867-5309")

        #test changing email address
        self.assertEqual(self.Account1.accountInfo["Email"], "chunkylover53@aol.com")
        self.Account1.setInfo("Email", "fakeemail@altavista.com")
        self.assertEqual(self.Account1.accountInfo["Email"], "fakeemail@altavista.com")

        #test changing Office Phone
        self.assertEqual(self.Account1.accountInfo["Office Phone"], "555-5555")
        self.Account1.setInfo("Office Phone", "123-4567")
        self.assertEqual(self.Account1.accountInfo["Office Phone"], "123-4567")

        #test changing office hours
        self.assertEqual(self.Account1.accountInfo["Office hours"], "All day everyday")
        self.Account1.setInfo("Office hours", "never")
        self.assertEqual(self.Account1.accountInfo["Office hours"], "never")

        #test changing password
        self.assertEqual(self.Account1.accountInfo["password"], "password")
        self.Account1.setInfo("password", "goodPassword")
        self.assertEqual(self.Account1.accountInfo["password"], "goodPassword")

        with self.assertRaises(ValueError):
            self.Account1.setInfo("height", "5'5")

    def test_getInfo(self):
        #test getting the address
        self.assertEqual(self.Account1.getInfo("address"), "123 Fake Street")

        #test getting the home phone
        self.assertEqual(self.Account1.getInfo("Home Phone"), "555-0113")

        #test getting title
        self.assertEqual(self.Account1.getInfo("title"), 0)

        #test getting email
        self.assertEqual(self.Account1.getInfo("Email"), "chunkylover53@aol.com")

        #test_getting_Office phone
        self.assertEqual(self.Account1.getInfo("Office Phone"), "555-5555")

        #test getting office hours
        self.assertEqual(self.Account1.getInfo("Office hours"), "All day everyday")

        #Should not work
        with self.assertRaises(ValueError):
            self.Account1.getInfo("height")

    def test_str(self):
        self.assertEqual(str(self.Account1), "Mr.Sparkle")






