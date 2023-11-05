from game_message import *
def GetClosestMeteorite(meteorites: List)->Meteor:
    prev = 1000000
    closest = None
    for meteorite in meteorites:
        if meteorite.position.x < prev:
            closest = meteorite
            prev = closest.position.x
    return closest
