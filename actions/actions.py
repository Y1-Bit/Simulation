import random
from abc import ABC, abstractmethod

from entities.herbivore import Herbivore
from entities.predator import Predator
from entities.static_objects import Grass, Rock, Tree
from map import Map


class Action(ABC):
    @abstractmethod
    def execute(self, game_map: Map) -> None:
        pass


class InitAction(Action):
    def execute(self, game_map: Map) -> None:
        self.spawn_static_entities(game_map, Grass, 4)
        self.spawn_static_entities(game_map, Rock, 5)
        self.spawn_static_entities(game_map, Tree, 5)
        self.spawn_creature(game_map, Herbivore, 1, 30)
        self.spawn_creature(game_map, Herbivore, 1, 30)
        self.spawn_creature(game_map, Predator, 2, 15, 5)

    def spawn_static_entities(self, game_map: Map, entity_type: type, count: int) -> None:
        for _ in range(count):
            while True:
                x, y = random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1)
                if not game_map.get_entity((x, y)):
                    game_map.add_entity(entity_type((x, y)))
                    break

    def spawn_creature(self, game_map: Map, creature_type: type, speed: int, hp: int, attack_power: int | None = None) -> None:
        while True:
            position = (random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1))
            if not game_map.get_entity(position):
                if attack_power:
                    game_map.add_entity(creature_type(position, speed=speed, hp=hp, attack_power=attack_power))
                else:
                    game_map.add_entity(creature_type(position, speed=speed, hp=hp))
                break


class TurnAction(Action):
    def execute(self, game_map: Map) -> None:
        entities = game_map.get_entities()
        for entity in list(entities.values()):  
            if isinstance(entity, Herbivore) or isinstance(entity, Predator):
                entity.make_move(game_map)
                
                

