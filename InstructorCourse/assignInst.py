from CurrentUserHelper import CurrentUserHelper
from Account.models import Account
from InstructorCourse.models import InstructorCourse
from Course.models import Course
from InstructorCourse.models import InstructorCourse


class assignInst():

    def assignInst(self, command):
        #cuh = CurrentUserHelper()
        #if cuh.getCurrentUserTitle() != 4:
        #   return "Permission denied. Only supervisors can assign instructor to courses"
        if len(command) > 3 or len(command) < 3:
            return "Please retype the command. " \
                   "assigninstructorcourse, courseNumber, userName "
        else:
            course = Course.objects.get(number=command[1])
            instructor = Account.objects.get(number=command[2])

            a = InstructorCourse()
            a.instructor = instructor
            a.course = course
            a.save()
            return "Assignment successfully completed"
