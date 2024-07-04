from __future__ import annotations

from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

from .entity import Entity

if TYPE_CHECKING:
    from map import Map

from strategies import PathFindingStrategy


class Creature(Entity, ABC):
    def __init__(self, position: tuple[int, int], speed: int, hp: int, path_finding_strategy: PathFindingStrategy) -> None:
        super().__init__(position)
        self.speed: int = speed
        self.hp: int = hp
        self.path_finding_strategy = path_finding_strategy

    @abstractmethod
    def make_move(self, game_map: Map) -> None:
        pass

    def is_next_to(self, target_position: tuple[int, int]) -> bool:
        dx: int = abs(self.position[0] - target_position[0])
        dy: int = abs(self.position[1] - target_position[1])
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1)

    def move_towards(
        self, game_map: Map, path: list[tuple[int, int]], creature_speed: int
    ) -> None:
        if not path or len(path) < 2:
            return

        if len(path) == 3 and creature_speed > 1:
            creature_speed = 1

        next_position_index = min(creature_speed, len(path) - 1)
        next_position = path[next_position_index]

        if (
            0 <= next_position[0] < game_map.width
            and 0 <= next_position[1] < game_map.height
            and game_map.get_entity(next_position) is None
        ):
            game_map.move_entity(self, next_position)
    
    def find_closest(self, game_map: Map, target_type: type) -> list[tuple[int, int]] | None:
        return self.path_finding_strategy.find_path(self.position, target_type, game_map)
