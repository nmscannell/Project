import unittest
from Commands import deleteAccount
from Commands import createAccount
import CourseCatalog

class test_deleteAccount(unittest.TestCase):

    def setUp(self):
        createAccount.createAccount("jimmy4", "TA", "jimmy4@uwm.edu")
        deleteAccount.deleteAccount("jimmy4", "TA")

    def test_account_deleted(self):
        self.assertTrue("jimmy4" not in CourseCatalog)



if __name__ == '__main__':
    unittest.main()
