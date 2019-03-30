from Account.models import Account
from CurrentUserHelper import CurrentUserHelper



class CreateAccount():

    def createAccount(self, command):
        CUH = CurrentUserHelper()
        if CUH.getCurrentUserTitle() < 4:
            return "Only Administrators can Create Accounts"
        if len(command) > 4 or len(command) < 4:
            return "createAccount takes 3 arguments: a userName, title and email"

        if Account.objects.get(userName=command[2]).exists():
            raise Exception("Account already exists")
        else:
            A = Account(userName=command[2], email=command[4])
            if command[3].lower() == "ta":
                A.title = 1
            elif command[3].lower() == "instructor":
                A.title = 2
            else:
                return "Invalid Title"
            A.save()
            return str(A) + " added to database"



" I changed the code to throw an exception if the account already exists, so it would be easier to test.  Instead of "
"having it throw an exception if it does not exist and then do the work, I couldn't figure out how to test it that way"
"""
        try:
            test = Account.objects.get(userName=command[2])
            return "Account already exists"
        except Account.DoesNotExist:
            A = Account(userName=command[2], email=command[4])
            if command[3].lower() == "ta":
                A.title = 1
            elif command[3].lower() == "instructor":
                A.title = 2
            else:
                return "Invalid Title"
            A.save()
            return str(A) + " added to database"
"""
