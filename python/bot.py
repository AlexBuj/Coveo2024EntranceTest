from game_message import *
from actions import *
from MeteorTargeted import *

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


        return [
            RotateAction(angle=15 * self.direction),
            ShootAction(),
        ]
