from simulation import Simulation


def main() -> None:
    width, height = 10, 10
    simulation = Simulation(width, height)
    try:
        simulation.start_simulation()
    except KeyboardInterrupt:
        print("\nGame stopped. Bye!")


if __name__ == '__main__':
    main()