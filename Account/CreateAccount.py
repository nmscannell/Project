from Account.models import Account
from CurrentUserHelper import CurrentUserHelper


class CreateAccount():

    def createAccount(self, command):
        CUH = CurrentUserHelper()
        if CUH.getCurrentUserTitle() < 4:
            return "You do not have the credentials to create an account. Permission denied"
        if len(command) > 4 or len(command) < 4:
            return "Your command is missing arguments, please enter your command in the following format: " \
                   "createAccount username title email"

        if Account.objects.filter(userName=command[1]).exists():
            return "Account already exists"
        else:
            A = Account.objects.create()
            A.userName = command[1]
            A.email = command[3]
            if command[2].lower() == "ta":
                A.title = 1
            elif command[2].lower() == "instructor":
                A.title = 2
            else:
                return "Invalid Title"
            A.save()
            #return str(A) + " added to database"
            return "Account successfully created"



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
