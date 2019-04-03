from django.test import TestCase
from Account.CreateAccount import CreateAccount
from Account.models import Account


class test_CreateAccount(TestCase):

    def setUp(self):
        self.CA = CreateAccount()
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

        self.command_create_account = ["createAccount", "data33", "instructor", "data33@starfleet.com"]
        self.command1_create_account = ["createAccount", "spock29", "instructor", "spock29@starfleet.com"]
        self.command2_create_account = ["createAccount", "tuckert90", "TA", "tuckert90@starfleet.com"]
        self.command_already_exists = ["createAccount", "picard304", "TA", "picardj@starfleet.com"]
        self.command2_already_exists = ["createAccount", "janewayk123", "instructor", "janewayk@starfleet.com"]
        self.command_missing_one_arg = ["createAccount", "parist64", "TA"]
        self.command_missing_two_args = ["createAccount", "paris64"]

    def test_account_successfully_created(self):
        CreateAccount.createAccount(self.CA, self.command_create_account)
        CreateAccount.createAccount(self.CA, self.command1_create_account)
        CreateAccount.createAccount(self.CA, self.command2_create_account)

        A = Account.objects.get(userName="data33")
        self.assertEqual(A.userName, "data33")
        self.assertEqual(A.email, "data33@starfleet.com")
        self.assertEqual(A.title, 2)

        B = Account.objects.get(userName="spock29")
        self.assertEqual(B.userName, "spock29")
        self.assertEqual(B.email, "spock29@starfleet.com")
        self.assertEqual(B.title, 2)

        C = Account.objects.get(userName="tuckert90")
        self.assertEqual(C.userName, "tuckert90")
        self.assertEqual(C.email, "tuckert90@starfleet.com")
        self.assertEqual(C.title, 1)

    def test_account_already_exist(self):
        self.assertEqual(CreateAccount.createAccount(self.CA, self.command_already_exists), "Account already exists")
        self.assertEqual(CreateAccount.createAccount(self.CA, self.command2_already_exists), "Account already exists")

    def test_missing_one_argument(self):
        self.assertEqual(CreateAccount.createAccount(self.CA, self.command_missing_one_arg),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createAccount username title email")

    def test_missing_two_arguments(self):
        self.assertEqual(CreateAccount.createAccount(self.CA, self.command_missing_two_args),
                         "Your command is missing arguments, please enter your command in the following format: "
                         "createAccount username title email")

