from Course.models import Course
from CurrentUserHelper import CurrentUserHelper


class CreateCourse():

    def createCourse(self, command):
        CUH = CurrentUserHelper()
        if CUH.getCurrentUserTitle() < 3:
            return "Only administrators and supervisors can create courses"
        if len(command) > 7 or len(command) < 7:
            return "Your command is missing arguments, please enter your command in the following form: " \
                   "createCourse courseName courseNumber onCampus daysOfWeek start end"

        if Course.objects.filter(number=command[2]).exists():
            return "Course already exists"
        else:
            c = Course(name=command[1], number=command[2])
            if command[3].lower() == "online":
                c.onCampus = False
            else:
                c.onCampus = True
                c.classDays = command[4]
                c.classHoursStart = command[5]
                c.classHoursEnd = command[6]
            c.save()
            return "Course successfully created"
