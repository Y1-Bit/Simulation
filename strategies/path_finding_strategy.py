from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from map import Map

class PathFindingStrategy(ABC):
    @abstractmethod
    def find_path(self, start: tuple[int, int], target_type: type, game_map: Map) -> list[tuple[int, int]] | None:
        pass