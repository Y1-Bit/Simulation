from simulation import Simulation
from actions import (
    Action,
    CheckAndSpawnAction,
    GenerateGrassAction,
    InitAction,
    TurnAction,
)
from renderer import ConsoleRenderer


def main() -> None:
    width, height = 10, 10
    renderer = ConsoleRenderer()
    init_actions: list[Action] = [InitAction()]
    turn_actions: list[Action] = [TurnAction(), GenerateGrassAction(), CheckAndSpawnAction()]
    simulation = Simulation(width, height, renderer, init_actions, turn_actions)
    try:
        simulation.start_simulation()
    except KeyboardInterrupt:
        print("\nGame stopped. Bye!")


if __name__ == "__main__":
    main()
