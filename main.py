# main.py
from src.training.trainer import run_training

if __name__ == "__main__":
    config = {"env_name": "CustomOpenEnv"}
    run_training(config)