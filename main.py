from simulation import Simulation


def main() -> None:
    width, height = 10, 10
    simulation = Simulation(width, height)
    simulation.start_simulation()


if __name__ == '__main__':
    main()