from collections import deque
from typing import TYPE_CHECKING

from .path_finding_strategy import PathFindingStrategy

if TYPE_CHECKING:
    from map import Map


class BreadthFirstSearchStrategy(PathFindingStrategy):
    def find_path(
        self, start: tuple[int, int], target_type: type, game_map: Map
    ) -> list[tuple[int, int]] | None:
        queue = deque([([start], start)])
        visited = set([start])

        entities = game_map.entities
        for entity in entities.values():
            if not isinstance(entity, target_type):
                visited.add(entity.position)

        while queue:
            path, current_position = queue.popleft()
            entity = game_map.get_entity(current_position)

            if entity and isinstance(entity, target_type) and current_position != start:
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
