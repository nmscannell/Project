from Lab.models import Lab
from CurrentUserHelper import CurrentUserHelper


class CreateLab():

    def createLab(self, command):
        cuh = CurrentUserHelper()
        if cuh.getCurrentUserTitle() < 3:
            return "Permission denied. Only administrators and supervisors can create labs"
        if len(command) > 5 or len(command) < 5:
            return "Please retype the command. " \
                   "CreateLabs command takes 5 arguments: course number,section number, meeting days, " \
                   "start time, and end time"
            courseNumber = command[1]
            sectionNumber = command[2]
            meetingDays = command[3]
            startTime = command[4]
            endTime = command[5]

            if Lab.objects.get(courseNumber).exists():
                raise Exception("Course number already exists")
            elif Lab.objects.get(sectionNumber).exists():
                raise Exception("Section number already exists")
            else:
                l = Lab(CourseNumber, Section)
                l.meetingDays = meetingDays
                l.classHoursStart = startTime
                l.classHoursEnd = endTime
                l.save()

            return str(c) + " added to database"