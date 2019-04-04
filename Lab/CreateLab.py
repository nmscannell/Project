from Lab.models import Lab
from Course.models import Course
from CurrentUserHelper import CurrentUserHelper


class CreateLab():

    def createLab(self, command):
        #cuh = CurrentUserHelper()
        #if cuh.getCurrentUserTitle() < 3:
        #    return "Permission denied. Only administrators and supervisors can create labs"
        if len(command) > 5 or len(command) < 5:
            return "Your command is missing arguments, please enter your command in the following format: " \
                   "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime"

        course = command[1]
        section = command[2]
        meeting = command[3]
        start = command[4]
        end = command[5]

        try:
            c = Course.objects.filter(course)
        except Course.DoesNotExist:
            return "The Course you are trying to create a lab for does not exist"

        if Lab.objects.filter(course, section).exists():
            return "Lab already exists, lab not added"
        else:
            l = Lab.objects.create()
            l.course = c
            l.sectionNumber = section
            l.meetingDays = meeting
            l.startTime = start
            l.endTi = end
            l.save()
            return "Lab successfully created"
