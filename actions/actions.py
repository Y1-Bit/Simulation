import random
from abc import ABC, abstractmethod

from entities import Grass, Herbivore, Predator, Rock, Tree
from map import Map
from strategies import PathFindingStrategy


class Action(ABC):
    @abstractmethod
    def execute(self, game_map: Map) -> None:
        pass


class EntityActions(Action, ABC):
    def spawn_creature(
        self,
        game_map: Map,
        creature_params: dict,
        path_finding_strategy: PathFindingStrategy,
    ) -> None:
        creature_type: type = creature_params['type']
        speed: int = creature_params['speed']
        hp: int = creature_params['hp']
        attack_power: int | None = creature_params.get('attack_power')

        while True:
            position = (
                random.randint(0, game_map.width - 1),
                random.randint(0, game_map.height - 1),
            )
            if not game_map.get_entity(position):
                if attack_power is not None:
                    game_map.add_entity(
                        creature_type(
                            position, speed=speed, hp=hp, attack_power=attack_power, path_finding_strategy=path_finding_strategy
                        )
                    )
                else:
                    game_map.add_entity(creature_type(position, speed=speed, hp=hp, path_finding_strategy=path_finding_strategy))
                break

    def spawn_static_entities(
        self, game_map: Map, entity_type: type, count: int
    ) -> None:
        for _ in range(count):
            while True:
                x, y = random.randint(0, game_map.width - 1), random.randint(
                    0, game_map.height - 1
                )
                if not game_map.get_entity((x, y)):
                    game_map.add_entity(entity_type((x, y)))
                    break


class InitAction(EntityActions):
    def __init__(
        self,
        herbivore_params: dict,
        predator_params: dict,
        grass_count: int,
        rock_count: int,
        tree_count: int,
        path_finding_strategy: PathFindingStrategy,
    ) -> None:
        self.herbivore_params = herbivore_params
        self.predator_params = predator_params
        self.grass_count = grass_count
        self.rock_count = rock_count
        self.tree_count = tree_count
        self.path_finding_strategy = path_finding_strategy

    def execute(self, game_map: Map) -> None:
        for _ in range(self.herbivore_params['count']):
            self.spawn_creature(game_map, self.herbivore_params, self.path_finding_strategy)
        for _ in range(self.predator_params['count']):
            self.spawn_creature(game_map, self.predator_params, self.path_finding_strategy)
        self.spawn_static_entities(game_map, Grass, self.grass_count)
        self.spawn_static_entities(game_map, Rock, self.rock_count)
        self.spawn_static_entities(game_map, Tree, self.tree_count)


class TurnAction(Action):
    def execute(self, game_map: Map) -> None:
        entities = game_map.entities
        for entity in list(entities.values()):
            if isinstance(entity, Herbivore) or isinstance(entity, Predator):
                entity.make_move(game_map)


class GenerateGrassAction(EntityActions):
    def __init__(self, generate_new_grass_count: int) -> None:
        self.generate_new_grass_count = generate_new_grass_count
    
    def execute(self, game_map: Map) -> None:
        grass_count = len(game_map.grasses)
        if grass_count == 0:
            self.spawn_static_entities(game_map, Grass, self.generate_new_grass_count)


class CheckAndSpawnAction(EntityActions):
    def __init__(self, check_and_spawn_params: dict, path_finding_strategy: PathFindingStrategy) -> None:
        self.check_and_spawn_params = check_and_spawn_params
        self.path_finding_strategy = path_finding_strategy

    def execute(self, game_map: Map) -> None:
        creatures = [
            entity
            for entity in game_map.entities.values()
            if isinstance(entity, (Herbivore, Predator))
        ]
        if len(creatures) <= 1:
            for _ in range(self.check_and_spawn_params['count']):
                self.spawn_creature(game_map, self.check_and_spawn_params, self.path_finding_strategy)
                
