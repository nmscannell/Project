from TACourse.models import TACourse
from Account.models import Account
from Course.models import Course


class AssignTACourse:

    def assignTACourse(self, command):
        if len(command) != 3:
            return "Your argument is missing commands, please enter your command in the following format: " \
                   "assignTACourse userName classNumber"

        if not Account.objects.filter(userName=command[1]).exists():
            return "Invalid account name"

        if not Course.objects.filter(number=command[2]).exists():
            return "Invalid course number"

        ta = Account.objects.get(userName=command[1])

        if ta.title > 1:
            return "Account is not a ta"

        course = Course.objects.get(number=command[2])
        l = TACourse()
        l.TA = ta
        l.Course = course
        l.save()

        return "Assignment successful"