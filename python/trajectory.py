import numpy as np
from game_message import *

def ProjectileToMatrix(projectile: Projectile)->np.array:
    position = np.array([projectile.position.x, projectile.position.y])
    velocity = np.array([projectile.velocity.x, projectile.velocity.y])
    return (position, velocity)