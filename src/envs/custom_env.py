# src/envs/custom_env.py
import gymnasium as gym
from gymnasium import spaces
import numpy as np

class CustomOpenEnv(gym.Env):
    metadata = {"render_modes": ["human"]}

    def __init__(self, render_mode=None):
        super().__init__()
        self.render_mode = render_mode

        # Define action space (for example, discrete)
        self.action_space = spaces.Discrete(4)

        # Define observation space (for example, 2D position)
        self.observation_space = spaces.Box(
            low=-10, high=10, shape=(2,), dtype=np.float32
        )

        self._max_steps = 1000
        self._steps = 0

    def reset(self, seed=None):
        super().reset(seed=seed)
        self._steps = 0
        self._agent_pos = np.array([0.0, 0.0])
        return self._agent_pos, {}

    def step(self, action):
        # Simple dynamics: move in 4 directions
        movement = np.array([[0,1], [0,-1], [1,0], [-1,0]])[action]
        self._agent_pos += movement

        reward = float(-np.linalg.norm(self._agent_pos))
        self._steps += 1
        truncated = self._steps >= self._max_steps
        terminated = False

        return self._agent_pos, reward, terminated, truncated, {}

    def render(self):
        if self.render_mode == "human":
            print(f"Agent pos: {self._agent_pos}")