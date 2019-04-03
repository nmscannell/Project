from Lab.models import Lab
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

        #if Lab.objects.get(courseNumber).exists():
        #    return "Course number already exists"
        if Lab.objects.filter(courseNumber, sectionNumber).exists():
            return "Lab already exists, lab not added"
        else:
            l = Lab(courseNumber, sectionNumber)
            l.meetingDays = meetingDays
            l.classHoursStart = startTime
            l.classHoursEnd = endTime
            l.save()
            return "Lab successfully created"