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
                    idOccurence = idOccurence + 1
            if(idOccurence == 0):
                self.targetedID.append(newMeteor.id)
            idOccurence = 0

    def removeMeteorIdFromList(self, id):
        self.targetedID.remove(id)