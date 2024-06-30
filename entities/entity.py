from abc import ABC


class Entity(ABC):
    def __init__(self, position: tuple[int, int]) -> None:
        self.position: tuple[int, int] = position