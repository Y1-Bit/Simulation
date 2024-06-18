from .creatures import Creature


class Herbivore(Creature):
    def __init__(self, position: tuple[int, int], speed: int, hp: int) -> None:
        super().__init__(position, speed, hp)

    def make_move(self) -> None:
        print('Herbivore moves')