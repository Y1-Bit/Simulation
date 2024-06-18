from .creatures import Creature
from .herbivore import Herbivore


class Predator(Creature):
    def __init__(self, position: tuple[int, int], speed: int, hp: int, attack_power: int) -> None:
        super().__init__(position, speed, hp)
        self.attack_power: int = attack_power

    def make_move(self) -> None:
        print('Predator moved to hunt.')
    
    def attack(self, herbivore: Herbivore) -> None:
        herbivore.hp -= self.attack_power 
        if herbivore.hp <= 0:
            print('Herbivore has been killed.')