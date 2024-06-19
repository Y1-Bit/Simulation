import random
from abc import ABC, abstractmethod

from entities.grass import Grass
from entities.herbivore import Herbivore
from entities.predator import Predator
from entities.static_objects import Rock, Tree
from map import Map


class Action(ABC):
    @abstractmethod
    def execute(self, game_map: Map) -> None:
        pass


class InitAction(Action):
    def execute(self, game_map: Map) -> None:
        for x in range(game_map.width):
            for y in range(game_map.height):
                if random.random() < 0.2: 
                    rand_value = random.random()
                    if rand_value < 0.4:  
                        game_map.add_entity(Grass((x, y)))
                    elif rand_value < 0.7:  
                        game_map.add_entity(Rock((x, y)))
                    else:  
                        game_map.add_entity(Tree((x, y)))
        initial_herbivore_position = (random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1))
        game_map.add_entity(Herbivore(initial_herbivore_position, speed=1, hp=10))
        initial_predator_position = (random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1))
        game_map.add_entity(Predator(initial_predator_position, speed=2, hp=15, attack_power=5))


class TurnAction(Action):
    def execute(self, game_map: Map) -> None:
        herbivores = game_map.get_entities_of_type(Herbivore)
        x, y = 0, 0
        for herbivore in herbivores:
            game_map.move_entity(herbivore, (x , y))

