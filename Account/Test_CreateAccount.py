from django.test import TestCase
from Account.CreateAccount import CreateAccount
from Account.models import Account
from main import models


class test_CreateAccount(TestCase):

    def setUp(self):
        CreateAccount.objects.create(userName="janewayk123", name="Kathryn Janeway", password="123456",
                                     email="janewayk@starfleet.com", title="instructor",
                                     address="14 Voyager Drive", city="Delta", state="Quadrant", zipCode="00000",
                                     officeNum="456", officePhone="555-555-5555", officeDays="TR",
                                     officeHoursStart="1300", officeHoursEnd="1400", currentUser="false")

        CreateAccount.objects.create(userName="picard304", name="Jean Luc Picard", password="90456",
                                     email="picardj@startfleet.com", title="TA", address="87 Enterprise Avenue",
                                     city="Alpha", state="Quadrant", zipCode="11111", officeNum="54",
                                     officePhone="777-777-7777", officeDays="W", officeHoursStart="0900",
                                     officeHoursEnd="1000", currentUser="false")



    def test_account_successfully_created(self):
        A = Account.objects.filter(userName="janewayk123")
        self.assertEqual(A.name, "Kathryn Janeway")
        self.assertEqual(A.password, "123456")
        self.assertEqual(A.email, "janewayk@starfleet.com")
        self.assertEqual(A.title, 2)
        self.assertEqual(A.address, "14 Voyager Drive")
        self.assertEqual(A.city, "Delta")
        self.assertEqual(A.state, "Quadrant")
        self.assertEqual(A.zipCode, 00000)
        self.assertEqual(A.officeNum, 456)
        self.assertEqual(A.officeDays, "TR")
        self.assertEqual(A.officeHoursStart, 1300)
        self.assertEqual(A.officeHoursEnd, 1400)
        self.assertEqual(A.currentUser, "false")


    "I don't know if this is correct - I want to make sure an exception is raised when we try and make an account " \
    "that already exists"
    def test_account_already_exist(self):
        with self.assertRaises(Exception):
            models.command("createAccount picard304 TA picardj@startfleet.com")
