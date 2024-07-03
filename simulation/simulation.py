import threading
import time

from actions import Action
from map import Map
from renderer import ConsoleRenderer


class Simulation:
    def __init__(
        self,
        width: int,
        height: int,
        render: ConsoleRenderer,
        init_actions: list[Action],
        turn_actions: list[Action],
    ) -> None:
        self.map = Map(width, height)
        self.move_counter = 0
        self.renderer = render
        self.init_actions = init_actions
        self.turn_actions = turn_actions
        self.health_stats: dict[str, int] = {}
        self.is_paused = False
        self.running = True

    def next_turn(self) -> None:
        if not self.is_paused:
            for action in self.turn_actions:
                action.execute(self.map)
            self.move_counter += 1
            self.update_health_stats()
            self.renderer.render(self.map, self.health_stats, self.move_counter)

    def start_simulation(self) -> None:
        for action in self.init_actions:
            action.execute(self.map)

        input_thread = threading.Thread(target=self.read_input)
        input_thread.start()

        try:
            while self.running:
                self.next_turn()
                time.sleep(1)
        except KeyboardInterrupt:
            print("\nSimulation stopped.")
        finally:
            self.running = False
            input_thread.join()

    def update_health_stats(self) -> None:
        self.health_stats = {
            f"{creature.__class__.__name__}_{index}": creature.hp
            for index, creature in enumerate(self.map.creatures)
        }

    def read_input(self) -> None:
        while self.running:
            user_input = input()
            if user_input == "":
                self.toggle_pause()

    def toggle_pause(self) -> None:
        self.is_paused = not self.is_paused
        print("Simulation paused." if self.is_paused else "Simulation resumed.")
