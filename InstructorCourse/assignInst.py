from Account.models import Account
from Course.models import Course
from InstructorCourse.models import InstructorCourse

# This class is for assigning instructor to course command
class assignInst():
    # this function takes one argument "command"
    # It will return the message "Instructor was successfully assigned to class, if it is successful pass and there are no error
    def assignInst(self, command):
        # The command will be the format: assigninstructorcourse userName courseNumber
        # If the arguments are more than 3 or less than 3. It will give you an error message
        if len(command) != 3:
            return "There are arguments missing, Please enter your command in the following format: "\
                    "assigninstructorcourse userName courseNumber"
        # If the course is not existed. It will give you an error message "Invalid course number"
        if not Course.objects.filter(number=command[2]).exists():
            return "Invalid course number"
        # If the username isn't existed. It will give you an error message "Invalid user name"
        if not Account.objects.filter(userName=command[1]).exists():
            return "Invalid user name"

        instructor = Account.objects.get(userName=command[1])
        course = Course.objects.get(number=command[2])
        # title represented as an integer where 4=supervisor 3=administrator
        # 2=Instructor 1=TA. 0=No current User
        # If the instructor's title is not "2", It will give you an error message "Account is not an instructor"
        if instructor.title != 2:
            return "Account is not an instructor"
        # If the course is already assigned, it will give you an error message "This class is already assigned"
        if InstructorCourse.objects.filter(Course=course).exists():
            return "This class is already assigned"
        # Otherwise(if there are no errors found), it will show you an message""Instructor was
        # successfully assigned to class and save it on the database.
        else:
            a = InstructorCourse()
            a.Instructor = instructor
            a.Course = course
            a.save()
            return "Instructor was successfully assigned to class"
