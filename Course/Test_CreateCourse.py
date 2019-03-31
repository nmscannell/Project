from django.test import TestCase
from Course.CreateCourse import CreateCourse
from Course.models import Course
from main import models
from CurrentUserHelper import CurrentUserHelper
from LoginHelper import LoginHelper

class Test_CreateCourse(TestCase):
    def setUp(self):
        Course.objects.create(name="Temporal Mechanics", number=784, onCampus=True,
                              classDays="MW", classHoursStart="08:00AM", classHoursEnd="9:45AM")
        Course.objects.create(name="Warp Theory", number=633, onCampus=False)

        def test_course_successfully_created(self):
            c = Course.objects.get(number=784)
            self.assertEqual(c.name, "Temporal Mechanics")
            self.assertEqual(c.onCampus, True)
            self.assertEqual(c.classDays, "MW")
            self.assertEqual(c.classHoursStart, "08:00AM")
            self.assertEqual(c.classHoursEnd, "9:45AM")
            d = Course.objects.get(number=633)
            self.assertEqual(d.name, "Warp Theory")
            self.assertEqual(d.onCampus, False)
            self.assertEqual(d.classDays, " ")
            self.assertEqual(d.classHoursStart, "00:00")
            self.assertEqual(d.classHoursEnd, "00:00")

        def test_course_already_exist(self):
            with self.assertRaises(Exception):
                models.command("createCourse 'Warp Theory' 633 Online")
