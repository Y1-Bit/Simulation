# Simulation

This project is a simulation of an ecosystem that includes various entities such as herbivores, predators, and static objects. The simulation runs in real-time, utilizing multithreading to manage the actions of entities and the visualization of the environment.

## Installation

To run this project, Python version 3.8 or higher is required.

1. Clone the repository:

```bash
git clone https://github.com/Y1-Bit/Simulation.git
```

2. Navigate to the project directory:

```bash
cd Simulation
```

## Running the Simulation

To start the simulation, execute the following command in the terminal:

```bash
python main.py
```


## Project Structure

- `actions/`: Module containing action classes that entities can perform.
- `entities/`: Module containing entity classes such as herbivores, predators, and static objects.
- `map/`: Module containing the map class where the simulation takes place.
- `renderer/`: Module for visualizing the simulation.
- `simulation/`: Module containing the simulation logic.
- `main.py`: The main file to run the simulation.
