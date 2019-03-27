from account import account
from Directory import Directory

"""
This method will need access to the directory as well. It will return the account upon a successful
log in or None if the account wasn't found or the password was incorrect. That way the Current user 
and user title can be updated. 
"""


def login(command, Directory, currentUser):
    if len(command) < 2 or len(command) > 2:
        raise ValueError("login takes two arguments, Username and Password")

    tempaccount = Directory.getAccount(command[0])
    if command[1] == tempaccount.accountInfo["password"]:
        currentUser = tempaccount
    else:
        raise ValueError("incorrect password")
