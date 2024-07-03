from abc import ABC, abstractmethod


class PathFindingStrategy(ABC):
    @abstractmethod
    def find_path(self, start: tuple[int, int], target_type: type, game_map) -> list[tuple[int, int]] | None:
        pass