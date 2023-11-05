import numpy as np
import random
from game_message import *

def ProjectileToMatrix(projectile: Projectile)->np.array:
    position = np.array([projectile.position.x, projectile.position.y])
    velocity = np.array([projectile.velocity.x, projectile.velocity.y])
    return (position, velocity)

def Preshoot(game_message: GameMessage)->Vector:
    maxX = game_message.constants.world.width
    maxY = game_message.constants.world.height
    x = maxX - 1
    y = random.randint(0, maxY)
    return Vector(x, y)



#return [
#        RotateAction(angle=15 * self.direction),
##        ShootAction(),
#   ]
>>>>>>> b261a632ddc2732ac0364484f14bc15d188cc792
