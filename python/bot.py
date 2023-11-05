from game_message import *
from actions import *
from MeteorTargeted import *
from Utility import *

import numpy as np

class Bot:
    def __init__(self):
        self.direction = 1
        self.meteorTargetedList = MeteorTarget()
        print("Initializing your super mega duper bot")

    def get_next_move(self, game_message: GameMessage):
        """
        Here is where the magic happens, for now the moves are not very good. I bet you can do better ;)
        """

        self.meteorTargetedList.addNewMeteorToList(game_message.meteors)
        meteorToChoose = game_message.meteors[0]
        for id in self.meteorTargetedList.targetedID:
            closestMeteor = 10000000
            for meteor in game_message.meteors:
                if(meteor.id == id):
                    if meteor.position.x - game_message.cannon.position.x < closestMeteor:
                        closestMeteor = meteor.position.x - game_message.cannon.position.x
                        meteorToChoose = meteor

        self.meteorTargetedList.removeMeteorIdFromList(meteorToChoose.id)

        theta = calcAngleShoot(game_message, meteorToChoose)
        if(theta != -90 and theta != None):
            print(theta)

        if (theta == None):
            theta = 0

        return [
            RotateAction(theta - game_message.cannon.orientation),
            ShootAction(),
        ]
