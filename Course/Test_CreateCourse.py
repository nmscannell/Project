from django.test import TestCase
from Course.CreateCourse import CreateCourse
from Course.models import Course
from main import models


class Test_CreateCourse(TestCase):
    def setUp(self):
        self.CC = CreateCourse()
        Course.objects.create(name="TemporalMechanics", number=784, onCampus=True,
                              classDays="MW", classHoursStart=1000, classHoursEnd=1100)

        Course.objects.create(name="WarpTheory", number=633, onCampus=False, classDays="TR",
                              classHoursStart=1200, classHoursEnd=1250)

        self.command_create_course = ["createCourse", "NebulaStudies", "432", "Campus", "MW", "1300", "1400"]
        self.command_create_course2 = ["createCourse", "StarshipDesign", "275", "Online", "NN", "0000", "0000"]
        self.command_course_already_exists = ["createCourse", "TemporalMechanics", "784", "Campus", "MW",
                                              "1000", "1100"]
        self.command_create_course_missing_args1 = ["createCourse", "ReplicatorStudies",
                                                    "809", "Campus", "MW", "2000"]
        self.command_create_course_missing_args2 = ["createCourse", "ReplicatorStudies", "809", "Campus", "MW"]
        self.command_create_course_missing_args3 = ["createCourse", "ReplicatorStudies", "809", "Campus"]
        self.command_create_course_missing_args4 = ["createCourse", "ReplicatorStudies", "809"]
        self.command_create_course_missing_args5 = ["createCourse", "ReplicatorStudies"]
        self.command_create_course_missing_args6 = ["createCourse"]


    def test_course_successfully_created(self):
        CreateCourse.createCourse(self.CC, self.command_create_course)
        CreateCourse.createCourse(self.CC, self.command_create_course2)

        A = Course.objects.get(name="NebulaStudies")
        self.assertEqual(A.name, "NebulaStudies")
        self.assertEqual(A.number, 432)
        self.assertEqual(A.onCampus, True)
        self.assertEqual(A.classDays, "MW")
        self.assertEqual(A.classHoursStart, 1300)
        self.assertEqual(A.classHoursEnd, 1400)

        B = Course.objects.get(name="StarshipDesign")
        self.assertEqual(B.name, "StarshipDesign")
        self.assertEqual(B.number, 275)
        self.assertEqual(B.onCampus, False)
        self.assertEqual(B.classDays, " ")
        self.assertEqual(B.classHoursStart, 0000)
        self.assertEqual(B.classHoursEnd, 0000)


    def test_create_course_already_exists(self):
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_course_already_exists)),
                         "Course already exists")


    def test_create_course_missing_args(self):
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args1)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args2)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args3)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args4)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args5)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")
        self.assertEqual((CreateCourse.createCourse(self.CC, self.command_create_course_missing_args6)),
                         "Your command is missing arguments, please enter your command in the following form: "
                         "createCourse courseName courseNumber onCampus daysOfWeek start end")

