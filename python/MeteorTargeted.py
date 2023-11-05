class MeteorTarget:
    def __init__(self, meteorsList):
        self.meteors = meteorsList
        self.targetedID = list()
    def isMeteorInObject(self, id):
        for meteor in self.meteors:
            if(meteor.id == id):
                return False
        return True
    def updateMeteor(self, meteor):
        for meteor in self.meteors:
            if (meteor.id == id):
                self.meteors.remove(meteor)
                self.meteors.append(meteor)
    def addMeteor(self, meteor):
        self.meteors.append(meteor)
    def updateMeteorList(self, meteorList):
        for meteor in meteorList:
            if (self.isMeteorInObject(meteor)):
