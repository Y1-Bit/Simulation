from map import Map

from .creatures import Creature
from .herbivore import Herbivore
from .static_objects import Rock, Tree, Grass


class Predator(Creature):
    def __init__(self, position: tuple[int, int], speed: int, hp: int, attack_power: int) -> None:
        super().__init__(position, speed, hp)
        self.attack_power: int = attack_power

    def make_move(self, game_map: Map) -> None:
        herbivore_position = self.find_closest(game_map, Herbivore, (Rock, Tree, Grass))
        if herbivore_position:
            self.move_towards(game_map, herbivore_position)
            if self.is_next_to(herbivore_position):
                herbivore = game_map.get_entity(herbivore_position)
                if isinstance(herbivore, Herbivore):
                    self.attack(herbivore, game_map)

    def attack(self, herbivore: Herbivore, game_map: Map) -> None:
        herbivore.hp -= self.attack_power
        if herbivore.hp <= 0:
            game_map.remove_entity(herbivore)