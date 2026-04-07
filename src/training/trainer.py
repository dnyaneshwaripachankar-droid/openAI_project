# src/training/trainer.py
import gymnasium as gym
from gymnasium import make
from src.envs import make_custom_env
from src.agents.simple_agent import SimpleAgent

def run_training(config):
    # env = make_custom_env()
    env = make_custom_env()  # or use your OpenEnv wrapper
    agent = SimpleAgent(env.action_space)

    num_episodes = 10
    for ep in range(num_episodes):
        obs, _ = env.reset()
        done = False
        while not done:
            action = agent.act(obs)
            obs, reward, terminated, truncated, _ = env.step(action)
            done = terminated or truncated
            if done:
                print(f"Episode {ep} finished with reward: {reward}")