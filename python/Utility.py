import numpy as np
from trajectory import *
def CalculateAngleToRotate(angleCannon, angleTarget):
    return angleTarget - angleCannon


def calcAngleShoot(game_message, meteor):
    initVelocity = game_message.constants.rockets.speed
    initPosition =  np.array([game_message.cannon.position.x, game_message.cannon.position.y])
    meteorPosition, meteorVelocity = ProjectileToMatrix(meteor)
    degToRad = 1 / np.pi * 1 / 180
    for theta in range(-90, 90):
        velProj = initVelocity * np.array([np.cos(degToRad * theta), np.sin(degToRad * theta)])
        posSolve = meteorPosition - initPosition
        matrixSolve = np.array([velProj, meteorVelocity])
        intersect = np.linalg.solve(matrixSolve, posSolve.T)

        if intersect[0] > 1000 or intersect[1] > 1000 or intersect[0] < 0 or intersect[1] < 0:
            continue
        if matrixSolve[0][0] * intersect[0] + initPosition[0] > 0 or matrixSolve[1][1] * intersect[1] + initPosition[
            1] > 0:
            continue
        return theta