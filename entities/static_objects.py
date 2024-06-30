from .entity import Entity


class StaticObject(Entity):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__(position)


class Rock(StaticObject):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__(position)


class Tree(StaticObject):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__(position)


class Grass(Entity):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__(position)
