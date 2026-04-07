import yaml
import random
import numpy as np


# 🔹 Load YAML configuration
def load_config(path="env_config.yaml"):
    try:
        with open(path, "r") as file:
            config = yaml.safe_load(file)
        return config
    except Exception as e:
        print(f"Error loading config: {e}")
        return None


# 🔹 Set random seed (important for reproducibility)
def set_seed(seed=42):
    random.seed(seed)
    np.random.seed(seed)


# 🔹 Get action name from index
def action_to_string(action):
    mapping = {
        0: "UP",
        1: "DOWN",
        2: "LEFT",
        3: "RIGHT"
    }
    return mapping.get(action, "UNKNOWN")


# 🔹 Convert position to string
def pos_to_string(position):
    return f"({position[0]}, {position[1]})"


# 🔹 Check if position is valid inside grid
def is_valid_position(pos, width, height):
    x, y = pos
    return 0 <= x < width and 0 <= y < height


# 🔹 Check if position is obstacle
def is_obstacle(pos, obstacles):
    return pos in obstacles


# 🔹 Print grid (for debugging)
def print_grid(agent_pos, goal_pos, obstacles, width, height):
    for i in range(height):
        row = ""
        for j in range(width):
            if [i, j] == agent_pos:
                row += " A "
            elif [i, j] == goal_pos:
                row += " G "
            elif [i, j] in obstacles:
                row += " X "
            else:
                row += " . "
        print(row)
    print("\n")


# 🔹 Calculate reward
def compute_reward(pos, goal_pos, rewards):
    if pos == goal_pos:
        return rewards.get("goal", 10)
    return rewards.get("step", -1)


# 🔹 Reset environment state
def reset_env(start_pos):
    return start_pos.copy()