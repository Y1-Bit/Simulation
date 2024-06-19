import time

from actions import Action, InitAction, TurnAction
from map import Map
from renderer import ConsoleRenderer


class Simulation:
    def __init__(self, width, height) -> None:
        self.map = Map(width, height)
        self.move_counter = 0
        self.renderer = ConsoleRenderer()
        self.init_actions: list[Action] = [InitAction()]
        self.turn_actions: list[Action] = [TurnAction()]

    def next_turn(self) -> None:
        for action in self.turn_actions:
            action.execute(self.map)
        self.move_counter += 1
        self.renderer.render(self.map)

    def start_simulation(self) -> None:
        for action in self.init_actions:
            action.execute(self.map)
        self.renderer.render(self.map)
        while True:
            time.sleep(1)
            self.next_turn()

    def pause_simulation(self) -> None:
        pass
