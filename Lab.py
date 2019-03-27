from Course import Course

class Lab(Course):

    def __init__(self, courseNumber = 1, sectionNumber = 1):
        super().__init__(courseNumber)
        self.sectionNumber = sectionNumber

    def getSection(self):
        pass

    def setSection(self, newSection):
        pass
