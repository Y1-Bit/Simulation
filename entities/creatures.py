from abc import ABC, abstractmethod

from .entity import Entity


class Creature(Entity, ABC):
    def __init__(self, position: tuple[int, int], speed: int, hp: int) -> None:
        super().__init__(position)
        self.speed: int = speed
        self.hp: int = hp

    @abstractmethod
    def make_move(self) -> None:
        pass
