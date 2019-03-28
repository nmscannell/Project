from Account.models import Account


class LoginHelper():

    def login(self, command):
        test = Account.objects.filter(currentUser=True)
        if len(test) > 0:
            return "A User is already logged in"

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

    def logout(self):
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
