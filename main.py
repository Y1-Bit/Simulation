import json

from actions import (
    Action,
    InitAction,
    TurnAction,
    GenerateGrassAction,
    CheckAndSpawnAction,
)
from config import Config
from renderer import ConsoleRenderer
from simulation import Simulation
from strategies import BreadthFirstSearchStrategy


def load_config(config_path: str) -> dict:
    with open(config_path, "r") as file:
        return json.load(file)


def main() -> None:

    config_file = load_config("config.json")
    config = Config(config_file)

    width, height = config.get_simulation_params()

    renderer = ConsoleRenderer()

    herbivore_params, predator_params, grass_count, rock_count, tree_count = (
        config.get_init_action_params()
    )

    path_finding_strategy = BreadthFirstSearchStrategy()

    init_action = InitAction(
        herbivore_params=herbivore_params,
        predator_params=predator_params,
        grass_count=grass_count,
        rock_count=rock_count,
        tree_count=tree_count,
        path_finding_strategy=path_finding_strategy,
    )

    init_actions: list[Action] = [init_action]

    check_and_spawn_params, generate_new_grass_count = config.get_turn_actions_params()

    turn_actions: list[Action] = [
        TurnAction(),
        CheckAndSpawnAction(check_and_spawn_params, path_finding_strategy),
        GenerateGrassAction(generate_new_grass_count),
    ]

    simulation = Simulation(width, height, renderer, init_actions, turn_actions)

    try:
        simulation.start_simulation()
    except KeyboardInterrupt:
        renderer.game_stopped_message()


if __name__ == "__main__":
    main()
