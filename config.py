from entities import Herbivore, Predator, Grass, Rock, Tree


class Config:
    def __init__(self, config_file: dict) -> None:
        self.config_file = config_file
        self.entity_classes = {
            "Herbivore": Herbivore,
            "Predator": Predator,
            "Grass": Grass,
            "Rock": Rock,
            "Tree": Tree,
        }

    def convert_params(self, params: dict) -> dict:
        params['type'] = self.entity_classes[params['type']]
        return params
    
    def get_simulation_params(self) -> tuple[int, int]:
        simulation_params = self.config_file["simulation"]
        return simulation_params["width"], simulation_params["height"]

    def get_init_action_params(self) -> tuple:
        init_entities = self.config_file["init_entities"]
        herbivore_params = self.convert_params(init_entities["herbivore"])
        predator_params = self.convert_params(init_entities["predator"])
        static_counts = init_entities["static_counts"]
        return (
            herbivore_params,
            predator_params,
            static_counts["grass_count"],
            static_counts["rock_count"],
            static_counts["tree_count"],
        )

    def get_turn_actions_params(self) -> tuple[dict[str, str | int], int]:
        actions = self.config_file["actions"]
        check_and_spawn_params = self.convert_params(actions["check_and_spawn_action"])
        generate_new_grass_count = actions["generate_new_grass_count"]
    
        return check_and_spawn_params, generate_new_grass_count
        
