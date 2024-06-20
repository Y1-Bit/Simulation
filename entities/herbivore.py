from map import Map
from entities import Grass

from .creatures import Creature


class Herbivore(Creature):
    def __init__(self, position: tuple[int, int], speed: int, hp: int) -> None:
        super().__init__(position, speed, hp)

    def make_move(self, game_map: Map) -> None:
        grass_position = self.find_closest(game_map, Grass)
        print(grass_position)
        if grass_position:
            self.move_towards(game_map, grass_position)
            # TODO: Check Description
            if self.position == grass_position:
                grass = game_map.get_entity(grass_position)
                if isinstance(grass, Grass):
                    self.eat(grass, game_map)
        print('Herbivore moves')
        
    def eat(self, grass: Grass, game_map: Map) -> None:
        print('Herbivore eats grass.')
        game_map.remove_entity(grass)
