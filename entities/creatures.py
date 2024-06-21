from typing import Optional, Tuple, Type
from abc import ABC, abstractmethod
from collections import deque

from map import Map

from .entity import Entity


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

    def find_closest(self, game_map, target_type, static_types):
        static_positions = game_map.get_static_entities_positions(static_types)
        queue = deque([self.position])
        visited = set([self.position]) | static_positions  

        while queue:
            current_position = queue.popleft()

            entity = game_map.get_entity(current_position)
            if isinstance(entity, target_type):
                return current_position

            x, y = current_position
            neighbors = [(x-1, y), (x+1, y), (x, y-1), (x, y+1)]
            for neighbor in neighbors:
                if (0 <= neighbor[0] < game_map.width and 0 <= neighbor[1] < game_map.height and
                        neighbor not in visited):
                    queue.append(neighbor)
                    visited.add(neighbor)

        return None
    
    def move_towards(self, game_map: Map, target_position: tuple[int, int]) -> None:
        if not target_position:
            return

        x, y = self.position
        target_x, target_y = target_position

        if x < target_x:
            new_position = (x + 1, y)
        elif x > target_x:
            new_position = (x - 1, y)
        elif y < target_y:
            new_position = (x, y + 1)
        else:  # y > target_y
            new_position = (x, y - 1)

        if 0 <= new_position[0] < game_map.width and 0 <= new_position[1] < game_map.height and game_map.get_entity(new_position) is None:
            game_map.move_entity(self, new_position)
                
                