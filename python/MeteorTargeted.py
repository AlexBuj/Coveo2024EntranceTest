class MeteorTarget:
    def __init__(self):
        self.targetedID = list()

    def getTargetedID(self):
        return self.targetedID
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