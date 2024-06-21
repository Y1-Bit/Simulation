from map import Map

from .creatures import Creature

from .static_objects import Rock, Tree, Grass

class Herbivore(Creature):
    def __init__(self, position: tuple[int, int], speed: int, hp: int) -> None:
        super().__init__(position, speed, hp)

    def make_move(self, game_map: Map) -> None:
        grass_position = self.find_closest(game_map, Grass, (Rock, Tree))
        if grass_position:
            self.move_towards(game_map, grass_position)
            if self.is_next_to(grass_position):
                grass = game_map.get_entity(grass_position)
                if isinstance(grass, Grass):
                    self.eat(grass, game_map)
    
        
    def eat(self, grass: Grass, game_map: Map) -> None:
        self.hp += 2
        game_map.remove_entity(grass)
