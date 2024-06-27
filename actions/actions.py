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
        for _ in range(4):  
            x, y = random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1)
            game_map.add_entity(Grass((x, y)))
        for _ in range(5): 
            x, y = random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1)
            game_map.add_entity(Rock((x, y)))
        for _ in range(5):  
            x, y = random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1)
            game_map.add_entity(Tree((x, y)))
        
        # TODO: Creature can't spawn in filled cell
        initial_herbivore_position = (random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1))
        game_map.add_entity(Herbivore(initial_herbivore_position, speed=1, hp=30))
        initial_predator_position = (random.randint(0, game_map.width - 1), random.randint(0, game_map.height - 1))
        game_map.add_entity(Predator(initial_predator_position, speed=2, hp=15, attack_power=5))


class TurnAction(Action):
    def execute(self, game_map: Map) -> None:
        herbivores: list[Herbivore] = game_map.get_creatures_by_type(Herbivore)
        predators: list[Predator] = game_map.get_creatures_by_type(Predator)

        creatures = []

        max_len = max(len(herbivores), len(predators))
        for i in range(max_len):
            if i < len(herbivores):
                creatures.append(herbivores[i])
            if i < len(predators):
                creatures.append(predators[i])

        for creature in creatures:
            creature.make_move(game_map)
                
                

