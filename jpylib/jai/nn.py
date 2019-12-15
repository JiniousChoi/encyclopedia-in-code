#!/usr/bin/python3
## author: jinchoiseoul@gmail.com


from math import tanh
from pysqlite2 import dbapi2 as sqlite


class searchnet:

    def __init__(self, dbname):
        self.con = sqlite.connect(dbname)

    def __del__(self):
        self.con.close()

    def maketables(self):
        self.con.execute('create table hiddennode(create_key)')
        self.con.execute('create table wordhidden(fromid,toid,strength)')
        self.con.execute('create table hiddenurl(fromid,toid,strength)')
        self.con.commit()

    def getstrength(self, fromid, toid, layer):
        pass

    def setstrength(self, fromid, toid, layer, strength):
        pass

    def generatehiddennode(self, wordids, urls):
        pass

    def getallhiddenids(self, wordids, urlids):
        pass

    def setupnetwork(self, wordids, urlids):
        pass

    def feedforward(self):
        pass
    
    def dtanh(y):
        return 1.0-y*y

    def backPropagate(self, targets, N=0.5):
        pass

    def trainquery(self, wordids, urlids, selectedurl):
        pass

    def updatedatabase(self):
        pass



import unittest


class NNTest(unittest.TestCase):
    def test_basics(self):
        pass


if __name__ == "__main__":

    unittest.main()
