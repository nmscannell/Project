from django.db import models
from Account.models import Account

# Create your models here.
class UI:
    """
    Here is where the string input from the command line is parsed. I currently have it set up so its
    checking the string in lower so that the commands wont be case sensitive. If you wish to add an additional
    command just add another "elif command[0].lower() == <commandName>" at the bottom. Make sure command
    returns a string.
    """

    def command(self, inStr):
        command = inStr.split(' ')

        if command[0].lower() == "login":

            if len(command) > 3 or len(command) < 3:
                return "login takes 2 arguments Account name and Password"

            try:
                CurrentUser = Account.objects.get(Name=command[1])
                if CurrentUser.password != command[2]:
                    return "Incorrect password"

            except Account.DoesNotExist:
                return "Account Not Found"

            CurrentUser.currentUser = True
            CurrentUser.save()
            return "Logged in as " + str(CurrentUser)

        elif command[0].lower() == "logout":
            try:
                CurrentUser = Account.objects.get(currentUser=True)
                CurrentUser.currentUser = False
                CurrentUser.save()
                return "Successfully logged out"
            except Account.DoesNotExist:
                return "Please Log in First"
            except Account.MultipleObjectsReturned:
                return "Multiple accounts Logged in, Something went terribly wrong"

            return "Successfully logged out"
        elif command[0].lower() == "createaccount":
            """
            The code for creating an account should go here. createAccount takes 2 additional arguments, the name
            and the title. These still be stored in command[1] and command[2]. Create account should check if an
            account with the same account name already exists in the databsae. If not, create the account otherwise 
            return an error message.  
            """
            return command[0]
        elif command[0].lower() == "createlab":
            """
            The code for creating a lab should go here. 
            """
            return command[0]
        elif command[0].lower() == "createcourse":
            """
            """
            return command[0]

        else:
            return command[0] + " is an unsupported command"

        return inStr


#class createCourse(models.model):
#    name = models.CharField(max_length=30)
#    number = models.CharField(max_length=3)
#    days = models.CharField(max_length=4)
#    start = models.CharField(max_length=4)
#    end = models.CharField(max_length=4)


