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
            """
            login should take 2 additional arguments, accountName and password, stored in commmand[1] and command[2]. 
            We need to check if the database contains the account name and if it does check if the passwords match.
            If the account exists and the passwords match the Current user will be updated to the account.
            Not sure how we want to implement a "current user" Ill think of something later maybe. 
            """
            return command[0]
        elif command[0].lower() == "logout":
            """
            The code for logout should go here. logout shouldn't need to take any additional arguments but if any
            other arguments are passed in, they are ignored. This should just wipe the current user and current user 
            privileges so that other commands cannot be accessed without logging in again. 
            """
            return command[0]
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


