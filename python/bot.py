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

        theta = calcAngleShoot(game_message, game_message.meteors[0])
        if(theta != -90 and theta != None):
            print(theta)

        if (theta == None):
            theta = 0
        return [
            RotateAction(theta),
            ShootAction(),
        ]
