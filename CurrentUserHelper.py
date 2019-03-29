from Account.models import Account


class CurrentUserHelper():

    def isCurrent(self):
        try:
            CurrentUser = Account.objects.get(currentUser=True)
            return True
        except Account.DoesNotExist:
            return False

    def getCurrentUser(self):
        try:
            CurrentUser = Account.objects.get(currentUser=True)
            return CurrentUser
        except Account.DoesNotExist:
            return None
    def getCurrentUserTitle(self):
        try:
            CurrentUser = Account.objects.get(currentUser=True)
            return CurrentUser.title
        except Account.DoesNotExist:
            return 0
