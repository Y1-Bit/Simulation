import json
from simulation import Simulation
from actions import (
    Action,
    CheckAndSpawnAction,
    GenerateGrassAction,
    InitAction,
    TurnAction,
)
from renderer import ConsoleRenderer
from entities import Herbivore, Predator, Grass, Rock, Tree

ENTITY_CLASSES = {
    "Herbivore": Herbivore,
    "Predator": Predator,
    "Grass": Grass,
    "Rock": Rock,
    "Tree": Tree,
}

def load_config(config_path: str) -> dict:
    with open(config_path, 'r') as file:
        return json.load(file)

def convert_params(params: dict) -> dict:
    params['type'] = ENTITY_CLASSES[params['type']]
    return params

def main() -> None:
    config = load_config('config.json')

    width = config["simulation"]["width"]
    height = config["simulation"]["height"]
    renderer = ConsoleRenderer()

    herbivore_params = convert_params(config["init_entities"]["herbivore"])
    predator_params = convert_params(config["init_entities"]["predator"])
    static_counts = config["init_entities"]["static_counts"]

    init_action = InitAction(
        herbivore_params=herbivore_params,
        predator_params=predator_params,
        grass_count=static_counts["grass_count"],
        rock_count=static_counts["rock_count"],
        tree_count=static_counts["tree_count"],
    )

    generate_new_grass_count = config["actions"]["generate_new_grass_count"]

    check_and_spawn_params = convert_params(config["actions"]["check_and_spawn_action"])

    init_actions: list[Action] = [init_action]
    turn_actions: list[Action] = [
        TurnAction(),
        CheckAndSpawnAction(check_and_spawn_params=check_and_spawn_params),
        GenerateGrassAction(generate_new_grass_count),
    ]
    simulation = Simulation(width, height, renderer, init_actions, turn_actions)
    try:
        simulation.start_simulation()
    except KeyboardInterrupt:
        renderer.game_stopped_message()

if __name__ == "__main__":
    main()
