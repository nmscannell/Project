from TACourse.models import TACourse
from Account.models import Account
from Course.models import Course


class AssignTACourse:
    """
    assignTACourse(self, command) takes a list of 3 strings in the format [command, username, class number]
        --command must be "assignTACourse"
        --username must be a valid username for a TA account that exists in the database
        --class number must be a valid class number for a course that exists in the database


    """

    def assignTACourse(self, command):
        if len(command) != 3:
            return "Your command has an incorrect number of arguments, please enter your command in the following format: " \
                   "assignTACourse userName classNumber"

        # search database for given username to make sure the account exists
        if not Account.objects.filter(userName=command[1]).exists():
            return "Invalid TA username."

        # search database for given course number to make sure the course exists
        if not Course.objects.filter(number=command[2]).exists():
            return "Invalid course number."

        ta = Account.objects.get(userName=command[1])

        # title designates privileges; 1 for TA. Make sure account with given username is a TA.
        if ta.title > 1:
            return "Account is not a TA."

        course = Course.objects.get(number=command[2])

        # Look for the TA assignment to see if the TA is already assigned to the course.
        if TACourse.objects.filter(TA=ta, Course=course).exists():
            return str(ta) + " is already assigned to " + str(course)

        # No errors--can go ahead and assign
        l = TACourse()
        l.TA = ta
        l.Course = course
        l.save()

        return "Assignment successful."
