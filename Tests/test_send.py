import unittest
from Commands import send


class test_send(unittest.TestCase):

    def setUp(self):
        self.send1 = send.send("eonshik")
        self.send2 = send.sendMultiple("eonshik spykim2003", "-s")
        self.send3 = send.sendAll("-a")

    def test_name(self):
        self.assertEqual(self.send1.getAccountName(), "eonshik")

    def test_multiple_names(self):
        self.assertEqual(self.send2.getAccountNames(), "eonshik spykim2003", "-s")

    def test_all(self):
        self.assertEqual(self.send3.getAccountNames(), "-a")

    def test_speicific_option(self):
       self.assertRaises(send.multiple, "eonshik, spykim2003")
       self.assertRaises(send.multiple, "eonshik, spykim2003")
       self.assertRaises(send.multiple, "eonshik : spykim2003")
       self.assertRaises(send.multiple, "eonshik ; spykim2003")
       self.assertRaises(send.multiple, "eonshik . spykim2003")
       self.assertRaises(send.multiple, "eonshikspykim2003")






       if __name__ == '__main__':
                 unittest.main()
