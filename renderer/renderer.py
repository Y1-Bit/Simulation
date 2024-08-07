import os

from entities import Grass, Herbivore, Predator, Rock, Tree
from map import Map


class ConsoleRenderer:
    def simulation_stopped(self) -> None:
        print("\nSimulation stopped.")
    
    def toggle_pause_message(self, is_paused: bool) -> None:
        print("Simulation paused." if is_paused else "Simulation resumed.")

    def game_stopped_message(self) -> None:
        print("\nGame stopped. Bye!")

    def clear_console(self) -> None:
        os.system("cls" if os.name == "nt" else "clear")

    def render(self, game_map: Map, health_stats: dict, move_counter: int) -> None:
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

        print("\nHealth Bar")
        for entity_type, total_health in health_stats.items():
            print(f"{entity_type}: {total_health} HP")

        print(f"\nMove: {move_counter}")
        print("\nPress Enter to pause/unpause the simulation")
        print("\nPress Ctrl+C to exit")
        
