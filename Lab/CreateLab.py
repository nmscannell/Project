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

        courseNumber = command[1]
        sectionNumber = command[2]
        meetingDays = command[3]
        startTime = command[4]
        endTime = command[5]

        try:
            c = Course.objects.filter(courseNumber)
        except Course.DoesNotExist:
            return "The Course you are trying to create a lab for does not exist"

        if Lab.objects.filter(courseNumber, sectionNumber).exists():
            return "Lab already exists, lab not added"
        else:
            l = Lab.objects.create()
            l.course = c
            l.sectionNumber=sectionNumber
            l.meetingDays = meetingDays
            l.startTime = startTime
            l.endTi = endTime
            l.save()
            return "Lab successfully created"
