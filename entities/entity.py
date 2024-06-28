from abc import ABC, abstractmethod


class Entity(ABC):
    def __init__(self, position: tuple[int, int]) -> None:
        self.position: tuple[int, int] = position