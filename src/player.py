class Player(object):
    
    def __init__(self, name: str) -> None:
        self.name = name
        self.items = {}
        self.current_room = None


def __repr__(self) -> str:
    return f"Player({repr(self.name)})"


def __str__(self) -> str:
    return f"{self.name.title()}\n{self.__dict__}"


def move(self, *args: str) -> None:
    if not args[0]:
        print("Please give me a valid direction \n")
        print("Directions are 'n', 's', 'e', 'w'\n")
        print("To move use command 'move' with directions desired \n")
        print("Example: To go North type 'move n'\n")
        return
    direction = args[0][0]
    if direction in ['n', 's', 'e', 'w']:
# no valid move available
        valid_move = eval(f'self.current_room.to_{direction}')
        if valid_move:
        # Removes player form room
            self.current_room.character.pop(self.name, None)
         # change current room to new room player moved to
            self.current_room = valid_move
        # Puts player into the new room
            self.current_room.players[self.name] = self

            if isinstance(valid_move):
                valid_move()
        else:
            ways = {'n': 'North', 's': 'South', 'e': 'East', 'w': 'West'}
            print(f"There is no path to the {ways[direction]}. \n")
            
        def print_position(self) -> None:
            print(f"{self.current_room.name} \n{self.current_room.description} \n")