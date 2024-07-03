from __future__ import annotations

from abc import ABC, abstractmethod
from collections import deque
from typing import TYPE_CHECKING

from .entity import Entity

if TYPE_CHECKING:
    from map import Map


class Creature(Entity, ABC):
    def __init__(self, position: tuple[int, int], speed: int, hp: int) -> None:
        super().__init__(position)
        self.speed: int = speed
        self.hp: int = hp

    @abstractmethod
    def make_move(self, game_map: Map) -> None:
        pass

    def is_next_to(self, target_position: tuple[int, int]) -> bool:
        dx: int = abs(self.position[0] - target_position[0])
        dy: int = abs(self.position[1] - target_position[1])
        return (dx == 1 and dy == 0) or (dx == 0 and dy == 1)

    def find_closest(self, game_map: Map, target_type: type) -> list[tuple[int, int]] | None:
        queue = deque([([self.position], self.position)])
        visited = set([self.position])

        entities = game_map.entities
        for entity in entities.values():
            if not isinstance(entity, target_type):
                visited.add(entity.position)

        while queue:
            path, current_position = queue.popleft()
            entity = game_map.get_entity(current_position)

            if (
                entity
                and isinstance(entity, target_type)
                and current_position != self.position
            ):
                return path

            x, y = current_position
            neighbors = [(x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)]
            for neighbor in neighbors:
                if (
                    0 <= neighbor[0] < game_map.width
                    and 0 <= neighbor[1] < game_map.height
                    and neighbor not in visited
                ):
                    new_path = path + [neighbor]
                    queue.append((new_path, neighbor))
                    visited.add(neighbor)

        return None

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
