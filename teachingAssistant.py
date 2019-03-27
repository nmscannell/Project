from instructor import instructor

"""
TAs can: 
-Edit their own contact information
-Read public contact information
-View TA assignments 
"""

class teachingAssistant(instructor):

    def __init__(self, name=""):
        super().__init__(name)
        self.accountInfo["title"] = 1
        self.labs = []
        self.accountInfo["Labs"] = self.labs
        self.graderStatus = False

    def addlab(self, newLab):
        self.accountInfo["Labs"] = self.labs.append(newLab)

    def displayCourses(self):
        for entry in self.labs:
            print(entry)


