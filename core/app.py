import typing
from itertools import product


class Character:
    def __init__(self, location: tuple, moves: list = []):
        self.location = location
        self.moves = moves

    @property
    def location(self):
        return self.location

    @location.setter
    def location(self, location: tuple, map: any):
        if location in map:
            pass

    def move(self, move: str) -> tuple:
        x, y = self.location
        if move == "up":
            y -= 1
        elif move == "down":
            y += 1
        elif move == "right":
            x += 1
        elif move == "left":
            x -= 1
        new_location = (x, y)
        return new_location

    def get_moves(self, dimensions: int) -> list:
        moves = ["up", "down", "right", "left"]
        x, y = self.location
        if x == 1:
            moves.remove("left")
        if x == (dimensions):
            moves.remove("right")
        if y == 1:
            moves.remove('up')
        if y == (dimensions):
            moves.remove("down")
        return moves


class Dragon(Character):

    def can_dragon_smell(distance: float, smelling_power: float) -> bool:
        if distance <= smelling_power:
            return True
        else:
            return False

    def can_dragon_see(distance: float, seeing_power: float) -> bool:
        if distance <= seeing_power:
            return True
        else:
            return False


class player(Character):
    pass


class Map:
    def __init__(self, dimensions: int) -> None:
        self.dimensions = dimensions

    @property
    def dimensions(self):
        return self.dimensions

    @dimensions.setter
    def dimensions(self, value: int):
        if value >= 0 and value <= 10:
            self.dimensions = value

    @property.getter
    def cells(self) -> list[tuple]:
        side = range(1, self.dimensions + 1)
        cells = [p for p in product(side, repeat=2)]
        return cells

def main():
    while True:
        command = input("Please Enter your command:\n")
        if command in valid_moves:
            pass
