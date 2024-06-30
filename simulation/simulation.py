import time

from actions import Action, InitAction, TurnAction, GenerateGrassAction, CheckAndSpawnAction
from map import Map
from renderer import ConsoleRenderer


class Simulation:
    def __init__(self, width, height) -> None:
        self.map = Map(width, height)
        self.move_counter = 0
        self.renderer = ConsoleRenderer()
        self.init_actions: list[Action] = [InitAction()]
        self.turn_actions: list[Action] = [TurnAction(), GenerateGrassAction(), CheckAndSpawnAction()]
        self.health_stats: dict[str, int] = {}
        self.is_paused = False
    
    def next_turn(self) -> None:
        if not self.is_paused:  
            for action in self.turn_actions:
                action.execute(self.map)
            self.move_counter += 1
            self.update_health_stats() 
            self.renderer.render(self.map, self.health_stats, self.move_counter)

    def start_simulation(self) -> None:
        for action in self.init_actions:
            action.execute(self.map)

        while True:
            self.next_turn()
            time.sleep(1)
        
    def update_health_stats(self) -> None:
        self.health_stats = {f"{creature.__class__.__name__}_{index}": creature.hp for index, creature in enumerate(self.map.creatures)}

    def pause_simulation(self) -> None:
        self.is_paused = True  

    def resume_simulation(self) -> None:
        self.is_paused = False  
