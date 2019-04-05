from Lab.models import Lab
from Course.models import Course
from CurrentUserHelper import CurrentUserHelper


class CreateLab():

    def createLab(self, command):
        if len(command) > 6 or len(command) < 6:
            return "Your command is missing arguments, please enter your command in the following format: " \
                   "createLab courseNumber labSectionNumber daysOfWeek beginTime endTime"

        courseNumber = command[1]
        sectionNumber = command[2]
        meetingDays = command[3]
        startTime = command[4]
        endTime = command[5]

        try:
            c = Course.objects.get(number=courseNumber)
        except Course.DoesNotExist:
            return "The Course you are trying to create a lab for does not exist"

        if Lab.objects.filter(course=c, sectionNumber=sectionNumber).exists():
            return "Lab already exists, lab not added"
        else:
            l = Lab.objects.create(course=c)

            l.sectionNumber = sectionNumber
            l.meetingDays = meetingDays
            l.startTime = startTime
            l.endTime = endTime
            l.save()
            return "Lab successfully created"
