# src/agents/simple_agent.py
import gymnasium as gym
import numpy as np

class SimpleAgent:
    def __init__(self, action_space: gym.Space):
        self.action_space = action_space

    def act(self, observation):
        return self.action_space.sample()