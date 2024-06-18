from .entity import Entity


class Grass(Entity):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__(position)