
class account():
    accountName = ""

    def __init__(self, accountName=""):
        self.accountName = accountName
        self.accountInfo = {
            "address": "",
            "password": "password",
            "Home Phone": "",
            "title": 0,
            "Email": "",
            "Office Phone": "",
            "Office hours": ""


        }

    def getName(self):
        return self.accountName

    def setName(self,newName):
        self.accountName = newName

    def setInfo(self, info, newInfo):
        if info in self.accountInfo:
            self.accountInfo[info] = newInfo
        else:
            raise(ValueError("Not a valid field"))

    def getInfo(self, info):
        if info in self.accountInfo:
            return self.accountInfo[info]
        else:
            raise (ValueError("Not a valid field"))

    def __str__(self):
        return self.accountName
