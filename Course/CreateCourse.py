from Course.models import Course
from CurrentUserHelper import CurrentUserHelper


class CreateCourse():

    def createCourse(self, command):
        CUH = CurrentUserHelper()
        if CUH.getCurrentUserTitle() < 3:
            return "Only administrators and supervisors can create courses"
        if len(command) > 5 or len(command) < 5:
            return "createCourse takes 5 arguments: course name, number, meeting days/online, start time, and end time"

        if Course.objects.get(number=command[3]).exists():
            raise Exception("Course already exists")
        else:
            c = Course(name=command[1], number=command[2])
            if command[3].lower() == "online":
                c.onCampus = False
            else:
                c.onCampus = True
                c.classDays = command[3]
                c.classHoursStart = command[4]
                c.classHoursEnd = command[5]
            c.save()
            return str(c) + " added to database"
