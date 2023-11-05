import numpy as np
from game_message import *

def ProjectileToMatrix(projectile: Projectile)->matrix:
    position = np.matrix(f'{projectile.position.x} {projectile.position.x}')
    velocity = np.matrix(f'{projectile.velocity.x} {projectile.velocity.x}')
    return (position,velocity)