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

        entities = self.map.get_entities()
        for entity in entities.values():
            if hasattr(entity, 'hp'):
                self.creatures.append(entity)
        
        while True:
            self.next_turn()
            time.sleep(1)
        
    def update_health_stats(self) -> None:
        self.health_stats = {creature.__class__.__name__: creature.hp for creature in self.creatures}

    def pause_simulation(self) -> None:
        self.is_paused = True  

    def resume_simulation(self) -> None:
        self.is_paused = False  
