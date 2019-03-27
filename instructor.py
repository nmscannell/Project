from account import account
"""
Instructors can: 
-Send out notifications to their TAs 
-Edit their own contact information
-Assign TAs to lab sections 
-View TA assignments 
-Read Public contact information
-View Course assignments 
"""


class instructor(account):

    def __init__(self, name=""):
        super().__init__(name)
        self.accountInfo["title"] = 2
        self.courses = []
        self.accountInfo["Courses"] = self.courses
        self.assignments = []

    def addcourse(self, newCourse):
        self.accountInfo["Courses"] = self.courses.append(newCourse)

    def displayCourses(self):
        for entry in self.courses:
            print(entry)

    def displayAssignments(self):
        for entry in self.assignments:
            print(entry)




