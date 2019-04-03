from InstructorCourse.models import InstructorCourse
from CurrentUserHelper import CurrentUserHelper


class assignInst():

    def assignInst(self, command):
        cuh = CurrentUserHelper()
        if cuh.getCurrentUserTitle() != 3:
            return "Permission denied. Only supervisors can assign instructor to courses"
        if len(command) > 2 or len(command) < 2:
            return "Please retype the command. " \
                   "assignInst command takes 2 arguments: classNumber, userName "
            classNumber = command[1]
            userName = command[2]

        if InstructorCourse.objects.get(classNumber).exists():
            raise Exception("Class number already exists")
        else:
            a = InstructorCourse(CourseNumber)
            l.userName = userName
            l.save()
            return str(c) + " added to database"