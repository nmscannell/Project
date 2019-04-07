from CurrentUserHelper import CurrentUserHelper
from Account.models import Account
from InstructorCourse.models import InstructorCourse
from Course.models import Course
from InstructorCourse.models import InstructorCourse


class assignInst():

    def assignInst(self, command):
        #cuh = CurrentUserHelper()
        #if cuh.getCurrentUserTitle() != 4:
        #   return "Permission denied. Only supervisors can assign instructor to courses"
        if len(command) < 3:
            return "Please, type the command in the following format assigninstructorcourse classNumber username"
        if not Course.objects.filter(userName=command[2]).exists():
            return "Please, type the course number"
        if not Account.objects.filter(number=command[1]).exists():
            return "Please, type your user name"
        instructor = Account.objects.get(userName=command[1])

        if instructor.title != 2:
            return "Account is not an instructor"

        course = Course.objects.get(number=command[1])
        instructor = Account.objects.get(userName=command[2])
        a = InstructorCourse()
        a.course = course
        a.instructor = instructor

        if InstructorCourse.objects.get(number=course).exists():
            return "Course is already assigned"
            a.save()
            return "Assignment successfully completed"
