# Implement a class to hold room information. This should have name and
# description attributes.
from collections import deque


class Room(object):

#TODO 2.2 The room should have `name` and `description` attributes.
#TODO 2.3 The room should also have `n_to`, `s_to`, `e_to`, and `w_to` attributes
    def __init__(self, name: str, description: str) -> None:
        self.name = name
        self.description = description
        self.items_ = {}
        self.characters = {}
        self.light = True
        self.to_n = None
        self.to_s = None
        self.to_w = None
        self.to_e = None


class Thunder_Dome(Room):

    def battle(self):
#fight until over
        battle_que = deque()

# Add the player and wolf to queue, have player attack first.
        for player in reversed(list(self.characters.keys())):
            battle_que.append(self.characters[player])

        if all(player.health > 0 for player in battle_que):
            print("OMG!! A WOLF!\n")
        else:
            print("\nThis is where I fought that wolf. And Won!! \n")
            return

        while not any(player.health <= 0 for player in battle_que):
            attacker = battle_que.popleft()
            attacked = battle_que.popleft()

            attacker.attack(attacked)
            if any([attacker.health <= 0, attacked.health <= 0]):
                break
            battle_que.append(attacked)
            battle_que.append(attacker)
