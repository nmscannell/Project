from Lab.models import Lab
from CurrentUserHelper import CurrentUserHelper


class CreateLab():

    def createLab(self, command):
        CUH = CurrentUserHelper()
        if CUH.getCurrentUserTitle() < 3:
            return "Only administrators and supervisors can create labs"
        if len(command) > 4 or len(command) < 4:
            return "createLabs takes 4 arguments: course number,section number, meeting days, start time, and end time"

       
            c.save()
            return str(c) + " added to database"