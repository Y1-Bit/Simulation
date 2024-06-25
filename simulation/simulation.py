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
        self.health_stats: dict[str, int] = {}
        self.creatures = []
    
    def next_turn(self) -> None:
        for action in self.turn_actions:
            action.execute(self.map)
        self.move_counter += 1
        self.update_health_stats() 
        self.renderer.render(self.map, self.health_stats)

    def start_simulation(self) -> None:
        for action in self.init_actions:
            action.execute(self.map)
        self.creatures = self.map.get_all_creatures()
        self.update_health_stats()
        self.renderer.render(self.map, self.health_stats)
        while True:
            time.sleep(1)
            self.next_turn()

        
    def update_health_stats(self) -> None:
        self.health_stats = {creature.__class__.__name__: creature.hp for creature in self.creatures}

    def pause_simulation(self) -> None:
        pass
