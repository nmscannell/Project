import unittest
from Commands import login
from instructor import instructor
from teachingAssistant import teachingAssistant
from Directory import Directory


class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.Directory = Directory()
        self.Instructor = instructor("Mr.Sparkle")
        self.Instructor.accountInfo["password"] = "12345"
        self.TA = teachingAssistant("Myopic Myron")
        self.TA.accountInfo["password"] = "54321"
        self.Directory.data.append(self.Instructor)
        self.Directory.data.append(self.TA)
        self.command1 = ["Mr.Sparkle", "12345"]
        self.command2 = ["Myopic Myron", "54321"]
        self.command3 = ["Mr.Sparkle", "444444"]
        self.command4 = ["I", "Dont", "know"]
        self.command5 = ["I"]


    def test_login(self):
        self.assertEqual(self.Instructor, login.login(self.command1, self.Directory))
        self.assertEqual(self.TA, login.login(self.command2, self.Directory))

        with self.assertRaises(ValueError):
            login.login(self.command3, self.Directory)


if __name__ == '__main__':
    unittest.main()
