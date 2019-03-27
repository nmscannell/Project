from account import account


class Directory():

    def __init__(self):
        self.data = []
        self.manyItems = 0

    def insert(self, newAccount):
        for i in self.data:
            if i.accountName == newAccount.accountName:
                raise ValueError(newAccount.accountName + " is already in the directory")
        self.data.append(newAccount)
        self.manyItems += 1

    def remove(self, account):
        return None

    def isEmpty(self):
        return len(self.data) == 0

    def getAccount(self, account):
        for i in self.data:
            if i.accountName == account:
                return i
        raise ValueError(account + " was not in the directory")
    def size(self):
        return self.manyItems
