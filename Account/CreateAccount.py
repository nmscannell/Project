from Account.models import Account
from CurrentUserHelper import CurrentUserHelper


class CreateAccount():

    def createAccount(self, command):

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
            return "Account successfully created"

