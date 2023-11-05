from game_message import *
from actions import *
<<<<<<< HEAD
from MeteorTargeted import *

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
        if game_message.cannon.orientation >= 45:
            self.direction = -1
        elif game_message.cannon.orientation <= -45:
            self.direction = 1
        print("PENIS")
        print(self.meteorTargetedList.targetedID)

        initVelocity = (1,1)
        initPosition = (0,0)
        for theta in range(-90,90):
            velProj = initVelocity @ np.array([[np.cos(0.5*theta/np.pi()),0],[0,[np.sin(0.5*theta/np.pi()),0]]])
            posSolve = posMeteor - initPosition
            matrixSolve = np.array([velProj, velMeteor])
            intersect = np.linalg.solve(matrixSolve,posSolve.T)

            if intersect[0] >1000 or intersect[1] > 1000 or intersect[0] <0 or intersect[1] <0:
                continue
            if matrixSolve[0][0] * intersect[0] + initPosition[0] >0 or matrixSolve[1][1] * intersect[1] + initPosition[1] >0:
                continue
            return theta

        return [
            RotateAction(angle=15 * self.direction),
            ShootAction(),
        ]
