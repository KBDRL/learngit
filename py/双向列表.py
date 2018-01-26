class Frob(object):
    def __init__(self, name):
        self.name = name
        self.before = None
        self.after = None
    def setBefore(self, before):
        # example: a.setBefore(b) sets b before a
        self.before = before
    def setAfter(self, after):
        # example: a.setAfter(b) sets b after a
        self.after = after
    def getBefore(self):
        return self.before
    def getAfter(self):
        return self.after
    def myName(self):
        return self.name

def insert(atMe, newFrob):
    """
    atMe: a Frob that is part of a doubly linked list
    newFrob:  a Frob with no links 
    This procedure appropriately inserts newFrob into the linked list that atMe is a part of.
    """
    # Your Code Here
    a = atMe.myName()[0]
    b = newFrob.myName()[0]
    aft = atMe.getAfter()
    #判断newFrob和atMe的位置
    while True:

        if a == b:
            newFrob.setBefore(atMe)
            if aft == None:
                atMe.setAfter(newFrob)
                break
            else:
                newFrob.setAfter(aft)
                atMe.setAfter(newFrob)
                aft.setBefore(newFrob)
                break

        #如果在atMe之后 继续判断 atMe的after是否还是在newFrob之后
        if a < b:
            if aft == None:
                newFrob.setBefore(atMe)
                atMe.setAfter(newFrob)
                break
            else:
                atMe = aft
                a = atMe.myName()[0]
                if a > b:
                    newFrob.setAfter(atMe)
                    newFrob.setBefore(atMe.getBefore())
                    atMe.getBefore().setAfter(newFrob)
                    atMe.setBefore(newFrob)
                    break

        #如果after为None或者 after大于newFrob 那么将 newFrob插入在after之前 而after插入在newFrob之后

        #如果after 或者atMe 与 newFrob相同 那么 newFrob插入在其后

        #如果在atMe之前 继续判断 atMe的before是否还在newFrob之后
        if a > b:
            if atMe.getBefore() == None:
                newFrob.setAfter(atMe)
                atMe.setBefore(newFrob)
                break
            else:
                atMe = atMe.getBefore()
                a = atMe.myName()[0]
                if a < b:
                    newFrob.setBefore(atMe)
                    newFrob.setAfter(atMe.getAfter())
                    atMe.getAfter().setBefore(newFrob)
                    atMe.setAfter(newFrob)
                    break
def findFront(start):
    """
    start: a Frob that is part of a doubly linked list
    returns: the Frob at the beginning of the linked list
    """
    #找到最初的forb
    be = start.getBefore()
    if be == None:
        return start
    else:
        return findFront(be)


eric = Frob('eric')
andrew = Frob('andrew')
ruth = Frob('ruth')
fred = Frob('fred')
martha = Frob('martha')

insert(eric, andrew)
insert(eric, ruth)
insert(eric, fred)
insert(ruth, martha)

# print(ruth.getAfter(), ruth.getBefore().myName())
# print(martha.getAfter().myName(), martha.getBefore().myName())
# print(fred.getAfter().myName(), fred.getBefore().myName())
# print(eric.getAfter().myName(), eric.getBefore().myName())
# print(andrew.getAfter().myName(), andrew.getBefore())

fin = findFront(ruth)
print(fin.myName())
