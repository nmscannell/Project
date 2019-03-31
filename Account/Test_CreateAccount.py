from django.test import TestCase
from Account.CreateAccount import CreateAccount
from Account.models import Account
from main import models
from CurrentUserHelper import CurrentUserHelper
from LogIn import LoginHelper




# How to test login permissions????

class test_CreateAccount(TestCase):

    def setUp(self):
        #Don't really get why we need these....
        self.CA = CreateAccount()
        self.LH = LoginHelper()
        Account.objects.create(userName="janewayk123", firstName="Kathryn", lastName = "Janeway", password="123456",
                                     email="janewayk@starfleet.com", title=2,
                                     address="14 Voyager Drive", city="Delta", state="Quadrant", zipCode="00000",
                                     officeNumber="456", officePhone="555-555-5555", officeDays="TR",
                                     officeHoursStart="1300", officeHoursEnd="1400", currentUser=False)

        Account.objects.create(userName="picard304", firstName="Jean Luc", lastName="Picard", password="90456",
                                     email="picardj@startfleet.com", title=1, address="87 Enterprise Avenue",
                                     city="Alpha", state="Quadrant", zipCode="11111", officeNumber="54",
                                     officePhone="777-777-7777", officeDays="W", officeHoursStart="0900",
                                     officeHoursEnd="1000", currentUser=False)

        Account.objects.create(userName = "kirkj22", firstName="James", lastName="Kirk", password="678543",
                               email="kirkj22@starfleet.com", title=4, address="789 Enterprise Avenue",
                               city="Alpha", state="Quadrant", zipCode="89765", officeNumber="987",
                               officePhone="897-654-398", officeDays="MW", officeHoursStart="1500",
                               officeHoursEnd="1600", currentUser=False)


    def test_account_successfully_created(self):
        self.command_create_account = ["createAccount", "data33", "instructor", "data33@starfleet.com"]
        CreateAccount.createAccount(self.CA, self.command_create_account)
        A = Account.objects.get(userName="data33")
        self.assertEqual(A.userName, "data33")
        self.assertEqual(A.email, "data33@starfleet.com")
        self.assertEqual(A.title, 2)


    def test_account_already_exist(self):
        LoginHelper.login(self.LH, ["login", "kirkj22", "678543"])
        self.command_already_exists = ["createAccount", "picard304", "TA", "picardj@starfleet.com"]
        self.command2_already_exists = ["createAccount", "janewayk123", "instructor", "janewayk@starfleet.com"]
        with self.assertRaises(Exception):
            CreateAccount.createAccount(self.CA, self.command_already_exists)
            CreateAccount.createAccount(self.CA, self.command2_already_exists)

    def test_missing_one_argument(self):
        LoginHelper.login(self.LH, ["login", "kirkj22" "678543"])
        self.command_missing_one_arg = ["createAccount", "parist64", "TA"]
        self.assertEqual(CreateAccount.createAccount(self.CA, self.command_missing_one_arg,
                                                     "createAccount takes 3 arguments: a userName, title and email"))

    def test_missing_two_arguments(self):
        LoginHelper.login(self.LH, ["login", "kirkj22", "678543"])
        self.command_missing_two_args = ["createAccount", "paris64"]
        self.assertEqual(CreateAccount.createAccount(self.CA, self.command_missing_two_args,
                                                     "createAccount takes 3 arguments: a userName, title and email"))

    def test_createAccount_permission(self):
        LoginHelper.login(self.LH, ["login", "janewayk123", "123456"])
        self.assertEqual(CreateAccount.createAccount(self.CA, ["paris64", "TA", "paris62@starfleet.com"]),
                         "Only Administrators can Create Accounts")
