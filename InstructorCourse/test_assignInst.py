class TestAssignInst(TestCase):
    def setUp(self):
        self.instructor1 = instructor()
        self.Course1 = Course(361)
        self.Course2 = Course(337)
        self.Lab1 = Lab(361, 804)

    def test_assignInst(self):
        self.assertEqual(len(self.instructor1.courses), 0)

        assignInst.assignInst(self.instructor1, self.Course1)

        self.assertEqual(len(self.instructor1.courses), 1)
        self.assertEqual(self.instructor1.courses[0], 361)

        assignInst.assignInst(self.instructor1, self.Course2, )

        self.assertEqual(len(self.instructor1.courses), 2)
        self.assertEqual(self.instructor1.courses[0], 361)
        self.assertEqual(self.instructor1.courses[1], 337)

        # Since lab is a type of Course we need to make sure an Inst cannot be assign to a lab
        with self.assertRaises(ValueError):
            assignInst.assignInst(self.instructor1, self.Lab1)