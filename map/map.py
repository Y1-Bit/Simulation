
from entities.entity import Entity


class Map:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.entities: dict[tuple[int, int], Entity] = {}

    def add_entity(self, entity: Entity) -> None:
        x, y = entity.position
        self.entities[(x, y)] = entity

    def get_entity(self, position: tuple[int, int]) -> Entity | None:
        return self.entities.get(position)

    def move_entity(self, entity: Entity, new_position: tuple[int, int]) -> None:
        if entity.position in self.entities:
            del self.entities[entity.position]
            entity.position = new_position
            self.entities[new_position] = entity

    def remove_entity(self, entity: Entity) -> None:
        if entity.position in self.entities:
            del self.entities[entity.position]

    # TODO: Fix type hints
    def get_creatures_by_type(self, type) -> list:
        return [creature for creature in self.entities.values() if isinstance(creature, type)]
