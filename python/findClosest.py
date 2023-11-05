from game_message import *
def GetClosestMeteorite(meteorites: List)->Meteor:
    prev = 0
    for meteorite in meteorites:
        if meteorite.position.x < prev:
            closest = meteorite
            prev = closest.x
    return closest
