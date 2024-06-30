from entities.entity import Entity
from entities.static_objects import Grass
from entities.creatures import Creature


class Map:
    def __init__(self, width: int, height: int) -> None:
        self.width: int = width
        self.height: int = height
        self.entities: dict[tuple[int, int], Entity] = {}
        self.grasses: set[Grass] = set()
        self.creatures: set[Creature] = set()

    def add_entity(self, entity: Entity) -> None:
        x, y = entity.position
        self.entities[(x, y)] = entity

        if isinstance(entity, Grass):
            self.grasses.add(entity)
        if isinstance(entity, Creature):
            self.creatures.add(entity)

    def get_entity(self, position: tuple[int, int]) -> Entity | None:
        return self.entities.get(position)

    def get_entities(self) -> dict[tuple[int, int], Entity]:
        return self.entities

    def move_entity(self, entity: Entity, new_position: tuple[int, int]) -> None:
        if entity.position in self.entities:
            del self.entities[entity.position]
            entity.position = new_position
            self.add_entity(entity)

    def remove_entity(self, entity: Entity) -> None:
        if entity.position in self.entities:
            del self.entities[entity.position]

            if isinstance(entity, Grass):
                self.grasses.remove(entity)
            if isinstance(entity, Creature):
                self.creatures.remove(entity)
