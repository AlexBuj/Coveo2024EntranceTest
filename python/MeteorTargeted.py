class MeteorTarget:
    def __init__(self):
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

    def addNewMeteorToList(self, newMeteorList):
        idOccurence = 0
        for newMeteor in newMeteorList:
            for meteorID in self.targetedID:
                if(newMeteor.id == meteorID):
                    idOccurence
            if(idOccurence == 0):
                self.targetedID.append(newMeteor)
            idOccurence = 0

    def removeMeteorIdFromList(self, id):
        self.targetedID.remove(id)

    def addMeteor(self, meteor):
        self.meteors.append(meteor)