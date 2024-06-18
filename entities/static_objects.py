from .entity import Entity


class StaticObject(Entity):
    def __init__(self, position: tuple[int, int]) -> None:
        super().__init__(position)


class Rock(StaticObject):
    pass


class Tree(StaticObject):
    pass
