# Implement a class to hold room information. This should have name and
# description attributes.

class Room:
    def __init__(self, name:str, description:str) -> None:
        self.name = name
        self.description = description
        self.to_n = None
        self.to_s = None
        self.to_w = None
        self.to_e = None
