import os

from entities import Grass, Herbivore, Predator, Rock, Tree
from map import Map



class ConsoleRenderer:
    def clear_console(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def render(self, game_map: Map) -> None:
        self.clear_console()
        for y in range(game_map.height):
            for x in range(game_map.width):
                entity = game_map.get_entity((x, y))
                if entity is None:
                    print("   ", end="")  
                elif isinstance(entity, Herbivore):
                    print("🐼 ", end="")  
                elif isinstance(entity, Predator):
                    print("🐯 ", end="")
                elif isinstance(entity, Grass):
                    print("🥦 ", end="")
                elif isinstance(entity, Rock):
                    print("🪨 ", end="")
                elif isinstance(entity, Tree):
                    print("🌲 ", end="")
            print()



