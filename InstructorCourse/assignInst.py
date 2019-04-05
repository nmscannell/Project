from InstructorCourse.models import InstructorCourse
from CurrentUserHelper import CurrentUserHelper
from Account.models import Account
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
        courseNumber = command[1]
        userName = command[2]

        try:
            c = Course.objects.get(number=courseNumber)
        except Course.DoesNotExist:
            return "The Course you are trying to assign a course for does not exist"

            a = InstructorCourse.objects.create()
            a.course = c
            a.courseNumber = courseNumber
            a.userName = userName
            a.save()
            return "Assignment successfully completed"
