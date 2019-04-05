from InstructorCourse.models import InstructorCourse
from CurrentUserHelper import CurrentUserHelper
from Course.models import Course
from InstructorCourse.models import InstructorCourse


class assignInst():

    def assignInst(self, command):
        #cuh = CurrentUserHelper()
        #if cuh.getCurrentUserTitle() != 3:
        #   return "Permission denied. Only supervisors can assign instructor to courses"
        if len(command) > 2 or len(command) < 2:
            return "Please retype the command. " \
                   "assignInst command takes 2 arguments: courseNumber, userName "
        courseNumber = command[1]
        userName = command[2]

        try:
            c = Course.objects.filter(command[1])
        except Course.DoesNotExist:
            return "The Course you are trying to assign a course for does not exist"

            a = InstructorCourse.objects.create()
            a.course = c
            a.classNumber = classNumber
            a.userName = userName
            l.save()
            return "Lab successfully created"
