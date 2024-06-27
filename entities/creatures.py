from abc import ABC, abstractmethod
from collections import deque

from .entity import Entity
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

    def find_closest(self, game_map: Map, target_type, ignore_types) -> list[tuple[int, int]] | None:
        ignore_positions = game_map.get_ignored_entities_positions(ignore_types)
        queue = deque([([self.position], self.position)])  
        visited = set([self.position]) | ignore_positions

        while queue:
            path, current_position = queue.popleft()

            entity = game_map.get_entity(current_position)
            if isinstance(entity, target_type):
                return path  

            x, y = current_position
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for neighbor in neighbors:
                if (0 <= neighbor[0] < game_map.width and 0 <= neighbor[1] < game_map.height and
                        neighbor not in visited):
                    new_path = path + [neighbor]  
                    queue.append((new_path, neighbor))
                    visited.add(neighbor)

        return None
    
    def move_towards(self, game_map: Map, path: list[tuple[int, int]], creature_speed: int) -> None:
        if not path or len(path) < 2:
            return

        next_position_index = min(creature_speed, len(path) - 1)
        next_position = path[next_position_index]

        if 0 <= next_position[0] < game_map.width and 0 <= next_position[1] < game_map.height and game_map.get_entity(next_position) is None:
            game_map.move_entity(self, next_position)
                    
                    