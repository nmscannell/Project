from Lab.models import Lab
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

            
            return str(c) + " added to database"