from player import Player
from mapping import rooms

#Parses user 
class Parser:
    def __init__(self) -> None:
        self.actions = ['move', 'look', 'get', 'drop', 'use', 'inventory', 'quit']
        self.directions = ['n', 's', 'e', 'w']
#prints player action list
    def print_actions(self) -> None:
        print(f'Available actions: {self.actions} \n')

#parse input and calls players method
    def parse(self, player: Player, commands: str) -> None:
        print(f"\nOkay, I'll try to {commands} \n")
        command = commands.split()

        if command[0] in self.actions:
            eval(f'player.{command[0]}({command[1:]})')
        else:
            print(f'Unknown action: {command[0]}')
            self.print_actions()
            player.print_position()
#contais player instantiation method and command parser method

class Game:


    def __init__(self):
        self.player = None
        self.parser = Parser()
#validate user input and instantiation to input to player
    def set_player(self, name: str = None, **kwargs) -> Player:
        if not name:
            while True:
                try:
                    name = input('\nWhat is your name? \n:')
                    if not name == "":
                        break
                    else:
                        print("I didn't catch that. \n")
                        continue
                except ValueError:
                    print("I didn't understand that. \n")
                    continue
        player = Player(name, **kwargs)
        if not self.player:
            self.player = player
        return player
#validate users input
    def get_player_input(self) -> None:

        parser = Parser()
        
        while True:
            try:
                command = input('What should I do? \n:')
            except ValueError as e:
                print("I didn't understand that. \n")
                print(e)
                continue
            else:
                if command.lower().startswith('q'):
                    break
                if command == "":
                    parser.print_actions()
                    continue
            parser.parse(self.player, command)
        print('Thanks for playing!')

#Sets up game
def main(rooms: dict) -> None:
    game = Game()

    game.set_player()
    game.player.current_room = rooms['empty_highway']
    rooms['empty_highway'].characters[game.player.name] = game.player

    wolf = game.set_player('The wolf', attack_points=20)
    wolf.current_room = rooms['stone_path']
    rooms['stone_path'].characters[wolf.name] = wolf
    print(f"\nThe Adventure Begins! \nGood luck {game.player.name}!!")

    puppy_dog = game.set_player('puppy_dog')
    rooms['puppy_dog'].characters[puppy_dog.name] = puppy_dog

    game.player.print_position()
    game.parser.print_actions()
    game.get_player_input()


if __name__ == '__main__':
    main(rooms)
