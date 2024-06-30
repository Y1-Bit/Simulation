from map import Map

from .creatures import Creature
from .static_objects import Grass


class Herbivore(Creature):
    def __init__(self, position: tuple[int, int], speed: int, hp: int) -> None:
        super().__init__(position, speed, hp)

    def make_move(self, game_map: Map) -> None:
        from .predator import Predator

        path_to_grass = self.find_closest(game_map, Grass)
        if path_to_grass:
            self.move_towards(game_map, path_to_grass, self.speed)
            if self.is_next_to(path_to_grass[-1]):
                grass_position = path_to_grass[-1]
                grass = game_map.get_entity(grass_position)
                if isinstance(grass, Grass):
                    self.eat(grass, game_map)

    def eat(self, grass: Grass, game_map: Map) -> None:
        self.hp += 2
        game_map.remove_entity(grass)
