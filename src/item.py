from player import Player


class Item(object):

    def __init__(self, name: str, description: str, weight: int = 0) -> None:
        self.name = name
        self.description = description
        self.is_light = False
        self.weight = weight
        self.active = False
        self.seen = False

    def __str__(self) -> str:
        return f"{self.name}, {self.description}"

    def __repr__(self) -> str:
        return self.description
    
#confirm added to inventory
    def on_get(self, *args) -> None:
        print(f"I have added the {self.name} to the inventory. \n")
        
#confirm dropped to inventory
    def on_drop(self) -> None:
        
        print(f"I have dropped the {self.name}")


class Container(Item):
    def __init__(self, name: str, description: str, weight: int = 0) -> None:
        super().__init__(name, description, weight)
        self.locked = False
        self.key = None
        self.items_ = {}


class SlingShot(Item):

    def __init__(self, name: str, description: str, weight: int, owner: Player = None) -> None:
        super().__init__(name, description, weight)
        self.owner = owner

#changes attack points with sling shot
    def shoot(self, character: Player) -> None:
        self.owner.attack_points += 30
        self.owner._attack(character)
        self.owner.attack_points -= 30

#Adds slings shot to inventory and change players utility
    def on_get(self, player: Player = None) -> None:
        self.owner = player
        self.owner.has_slingshot = True
        super().on_get()
        if not self.owner.has_rocks:
            print("Sweet! Now I need some ammo! \n")

# message when you try to shoot without ammo in inventory
    def blank(self):
        if not self.owner.has_rocks:
            print("Sorry out have no ammo\n")
        else:
            print("No ammo to use\n")


class Rocks(Item):

    def __init__(self, name: str, description: str, weight: int, owner: Player = None) -> None:
        super().__init__(name, description, weight)
        self.owner = owner

   #update having rocks
    def on_get(self, player: Player = None) -> None:
   
        self.owner = player
        self.owner.has_rocks = True
        super().on_get()

    def rock(self):
        
        print("I'm a rock")


class Berries(Item):

    def __init__(self, name: str, description: str, weight: int = 3) -> None:
        super().__init__(name, description, weight)
        self.owner = None

#updated having berries
    def on_get(self, player: Player = None) -> None:
        self.owner = player
        super().on_get()

#increase health
    def eat(self):
        old = self.owner.health
        # Remove berries from inventory and increase health.
        self.owner.health += 15
        self.owner.weight -= self.weight
        self.owner.items_.pop(self.name, None)
        print(f"{self.owner.name} health has gone from {old} to {self.owner.health} \n")
