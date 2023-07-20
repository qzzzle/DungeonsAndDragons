from __future__ import annotations
from abc import ABC, abstractmethod
from itertools import product
import random

COMMANDS = ["q"]

class character():
    def __init__(self, location: tuple) -> None:
        self.location = location

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
        self.location = new_location
        return new_location

    
class Player(character):
    _player_state = None
    def __init__(self, player_state: PlayerState) -> None:
        self.player_state = ExploringState()
        self.found_door = False
        self.entered_dragon_room = False
        self.change_state(player_state)

    def change_state(self, player_state: PlayerState):
        print(f"Player: Transition to {type(player_state).__name__}")
        self._player_state = player_state
        self._player_state.player = self


    def request_move(self):
        self._player_state.handle_move()

    def request2(self):
        self._player_state.handle2()

    def handle_input(self, valid_moves):
        self._player_state.handle_input(valid_moves)

    def enter(self):
        self._player_state.enter(self)



class PlayerState(ABC):

    @property
    def player(self) -> Player:
        return self._player

    @player.setter
    def player(self, player: Player) -> None:
        self._player = player

    @abstractmethod
    def handle_move(self) -> None:
        pass

    @abstractmethod
    def handle2(self) -> None:
        pass

    @abstractmethod
    def handle_input(self, valid_moves) -> None:
        pass

    @abstractmethod
    def enter(self) -> None:
        pass
    

class ExploringState(PlayerState):
    def handle_move(self) -> None:
        self.player.change_state(ExploringState())

    def handle_input(self, valid_moves: list[str]):
        move = input(f"You can move in {valid_moves}\nEnter your move: ").lower()
        if move in valid_moves:
            print(f"You moved {move}.")
            player.move(move)
            print(f"now you are in room {player.location}")
        elif move in COMMANDS:
            player.change_state(CommandingState())
        else:
            print("Invalid move. Please try again.")

    def handle2(self) -> None:
        pass
    def enter(self) -> None:
        return super().enter()

class CommandingState(PlayerState):
    pass

class ConcreteStateB(PlayerState):
    def handle_move(self) -> None:
        pass

    def handle2(self) -> None:
        self.player.change_state(ExploringState())




class LosingState(PlayerState):
    def enter(self):
        print("You entered the dragon's room! Game over.")



class WinningState(PlayerState):
    def enter(self):
        print("You found the door! You win the game.")


class EndingGameState(PlayerState):
    pass



class Dragon(character):
    def __init__(self, location: tuple=(0, 0)) -> None:
        super().__init__(location)
class DragonState():
    pass
class DragonIsSeeingState(DragonState):
    pass
class DragonISmellingState(DragonState):
    pass



def get_locations(cells: list[tuple]) -> tuple:
    return random.sample(cells, k=3)


def generate_cells(dimensions: int) ->list[tuple]:
    side = range(1, dimensions+1)
    cells = [p for p in product(side, repeat=2)]
    return cells

def get_moves(location: tuple, dimensions: int) -> list:
    moves = ["up", "down", "right", "left"]
    x, y = location
    if x == 1:
        moves.remove("left")
    if x == (dimensions):
        moves.remove("right")
    if y == 1:
        moves.remove('up')
    if y == (dimensions):
        moves.remove("down")
    return moves


if __name__ == "__main__":
    # The client code.
    dimensions = int(input("Please Enter the dimensions of the map you want to play in:"))
    cells = generate_cells(dimensions)
    player = Player(ExploringState())
    dragon = Dragon()
    player.location, dragon.location , door_location = get_locations(cells)
    while True:
        print(f"player:{player.location}\ndragon:{dragon.location}\ndoor:{door_location}")
        valid_moves = get_moves(player.location, dimensions)
        player.handle_input(valid_moves)
        if player.location == dragon.location:
            player.change_state(LosingState)
            player.enter()
            break
        elif player.location == door_location:
            player.change_state(WinningState)
            player.enter()
            break
        
    # player.request2()
    # player.request_move()