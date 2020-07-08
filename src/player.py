# Write a class to hold player information, e.g. what room they are in currently.
import random
import sys
from room import Thunder_Dome


class Player(object):


    def __init__(self, name: str, health: int = 100, attack_points: int = 5, weight_limit: int = 100) -> None:
        self.name = name
        self.items_ = {}
        self.current_room = None
        self.health = health
        self.attack_points = attack_points
        self.weight = 0
        self.weight_limit = weight_limit
        self.has_slingshot = False
        self.has_rocks = False

    def __repr__(self) -> str:
        return f"Player({repr(self.name)})"

    def __str__(self) -> str:
        return f"{self.name.title()}\n{self.__dict__}"

#Moving the player to room and direction
    def move(self, *args: str) -> None:
      
        # invalid move by player
        if not args[0]:
            print("Please tell me where you want to move. \n")
            print("Valid directions are 'n', 's', 'e', 'w'")
            print("To move North type: 'move n' \n")
            return
        direction = args[0][0]
        if direction in ['n', 's', 'e', 'w']:
            # Returns None if no room exists where the player wants to go.
            valid_move = eval(f'self.current_room.to_{direction}')
            if valid_move:
                
                # Remove the player from the current room.
                self.current_room.characters.pop(self.name, None)
                # Change the current room to the one desired.
                self.current_room = valid_move
                # Put the player in the new room.
                self.current_room.characters[self.name] = self
                # Deduct health according to the story.
                if self.current_room.name == 'small_pond':
                    self.health -= 10
                # Tell the player about the new room.
                self.print_position()
                # If we're in The wolf's room, do that stuff.
                if isinstance(valid_move, Thunder_Dome):
                    valid_move.battle()
            # If the player has asked to go somewhere that doesn't exist help 'em out.
            else:
                ways = {'n': 'North', 's': 'South', 'w': 'West', 'e': 'East'}
                print(f"There is no path to the {ways[direction]}. \n")

    def print_position(self) -> None:
       #prints room details 
        print(f"{self.current_room.name} \n{self.current_room.description} \n")

    def look(self, *args) -> None:
 
        # Check to see if the lights are on.
        if self.current_room.light or any(item.is_light and item.active for item in self.items_.values()):
            self.current_room.light = True
            if self.current_room.items_:
                print("I can see:")
                for val in self.current_room.items_.values():
                    val.seen = True
                    print(val)
            else:
                print(f"There is nothing to see\n")
        else:
            print("It is far to dark in here. \n")
        print()  # Just a blank line for display purposes.

    def get(self, *args: str) -> None:
     #Collect items with args
        if not args[0]:
            print("Please tell me what you want to get. \n")
            return
        item_name = args[0][0]
        # If the item is in this room and we have looked around.
        if item_name in self.current_room.items_ and self.current_room.items_[item_name].seen:
            item = self.current_room.items_[item_name]
            
      # Check that the Item won't cause us to exceed the weight limit.
            if self.weight + item.weight <= self.weight_limit:
                # Add the item to the inventory
                self.items_[item.name] = item
                self.weight += item.weight
                # Remove the item from the room.
                self.current_room.items_.pop(item.name, None)
                # Do whatever items do.
                item.on_get(self)
            else:
                print(f"I'm carrying too much weight to add {item.name}")
                print(f"Current inventory weight: {self.weight}")
                print(f"Item weight: {item.weight}")
                print(f"Current weight limit: {self.weight_limit} \n")
        else:
            print(f"I haven't seen {'an' if item_name.startswith(('a', 'e', 'i', 'o', 'u')) else 'a'} {item_name} \n")

#drop items in current room
    def drop(self, *args: str) -> None:
        if not args[0]:
            print("Please tell me what you want to drop. \n")
            return
        item_name = args[0][0]
        
        # checks for items
        if item_name in self.items_:
            item = self.items_[item_name]
            # drops nowhere
            self.items_.pop(item.name, None)
            self.weight -= item.weight
            # Move it from nowhere into the current room.
            self.current_room.items_[item.name] = item
            print(f"I have dropped {item.name} \n")
        else:
            print(f"I don't have {'an' if item_name.startswith(('a', 'e', 'i', 'o', 'u')) else 'a'} {item_name} \n")

#calls attack helper
    def attack(self, character: 'Player') -> None:
        if self.has_rocks and self.has_slingshot:
            self.items_['sling_shot'].shoot(character)
        else:
            self._attack(character)

#attacks characters
    def _attack(self, character: 'Player') -> None:
 
        # If a ten sided die comes up odd, it's a hit.
        if random.randint(0, 10) & 1:
            character.health -= self.attack_points
            if character.health <= 0:
                character.die()
            print(f"{self.name} {'shoots' if self.has_slingshot and self.has_rocks else 'hits'} "
                  f"{character.name}! Their health is now {character.health} \n")
        else:
            print(f"{self.name} missed! \n")

#Utilized items
    def use(self, *args: str) -> None:
        if not args[0]:
            print("Please tell me what you want to use. \n")
            return
        item_name = args[0][0]
        # Call item methods by matching strings.
        if item_name in self.items_:
            self.items_[item_name].active = True
        if 'key' in item_name:
            self._unlock_box(item_name)
        if 'sling' in item_name:
            self.items_[item_name].blank()
        if 'pebble' in item_name:
            self.items_[item_name].rock()
        if 'dog' in item_name:
            if 'puppy_dog' in self.current_room.characters:
                print(f"You found the dog and gave them a treat! They'll be your friend forever now. "
                      f"You win! \n")
                sys.exit()
            else:
                print("I don't see any dogs around here. \n")
        if 'berries' in item_name:
            # Ensure the specific berry is in inventory.
            if item_name in self.items_:
                self.items_[item_name].eat()

    def _unlock_box(self, key_name: str) -> None:
     
        shape = key_name.split('_')[0]
        # Check that the correct shape box is in the current room.
        if eval(f"'{shape}_lock_box' in self.current_room.items_"):
            box_name = f"{shape}_lock_box"
            # Check that the box has been seen and that the key is correct.
            if (self.current_room.items_[box_name].seen and
                    self.current_room.items_[box_name].key is self.items_[key_name]):
                # Unlock the box.
                self.current_room.items_[box_name].locked = False
                # Add contents of box to the room.
                for item in self.current_room.items_[box_name].items_.values():
                    self.current_room.items_[item.name] = item
                print(f"I have unlocked the {box_name} \n")
            else:
                print(f"I don't see anything that this key fits. \n")
        else:
            print(f"I don't see anything that this key fits. \n")

    def die(self) -> None:
       #player dies and scatters inventroy
       
        for item in self.items_.values():
            # Add inventory to current room.
            self.current_room.items_[item.name] = item
        # End the game if the player dies.
        if not self.name == 'The wolf':
            print(f"{self.name} has died! Now littered about the area "
                  f"are {[item.name for item in self.items_.values()]} \n")
            sys.exit()
        else:
            print("Take that The wolf! I win! \n")

    def inventory(self, *args) -> None:
      # Prints inventory list
        print(f"{self.name} - Current Health: {self.health}")
        print(f"Current Weight: {self.weight} / {self.weight_limit}")
        print("Items:")
        if self.items_:
            for item in self.items_.values():
                print(f'{item.name} - Weight: {item.weight}')
        else:
            print("I don't seem to have anything.")
        print()  # Blank line for display purposes.
