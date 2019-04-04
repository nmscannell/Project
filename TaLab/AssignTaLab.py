from TaLab.models import TaLab
from Account.models import Account
from Lab.models import Lab
from Course.models import Course


class AssignTaLab():

    def assignTaLab(self, command):
        if not Account.objects.filter(userName=command[1]).exists():
            return "Invalid account name"

        if not Course.objects.filter(number=command[2]).exists():
            return "Invalid course number"

        if not Lab.objects.filter(sectionNumber=command[3]).exists():
            return "Invalid lab section"
