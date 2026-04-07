import gymnasium as gym
import numpy as np
from typing import Tuple, Dict, Any
from types import YourAction, YourObservation

class YourEnv(gym.Env):
    """
    Structural Safety Digital Twin Environment.
    The agent must maintain structural integrity by adjusting 
    active damping or alerting for maintenance.
    """
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 30}

    def __init__(self, render_mode=None):
        super(YourEnv, self).__init__()
        
        # 1. Action Space: Discrete actions (0: Do Nothing, 1: Increase Damping, 2: Emergency Alert)
        self.action_space = gym.spaces.Discrete(3)

        # 2. Observation Space: [Stress Level, Vibration Frequency, Displacement]
        # Range normalized between 0 and 1
        self.observation_space = gym.spaces.Box(
            low=0, high=1, shape=(3,), dtype=np.float32
        )

        self.render_mode = render_mode
        self.state = None

    def reset(self, seed=None, options=None) -> Tuple[np.ndarray, Dict[str, Any]]:
        """Resets the twin to a baseline safety state."""
        super().reset(seed=seed)
        
        # Start with a safe, randomized baseline
        self.state = np.array([0.1, 0.2, 0.05], dtype=np.float32)
        
        info = {"status": "Monitoring Initialized"}
        return self.state, info

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, bool, Dict[str, Any]]:
        """Applies an action and returns the new sensor state."""
        stress, vibration, displacement = self.state

        # Environment Dynamics: Stress naturally fluctuates
        stress += np.random.normal(0.01, 0.02)
        vibration += np.random.normal(0.005, 0.01)

        # Apply Agent Action
        if action == 1:  # Active Damping
            vibration -= 0.05
            stress -= 0.01
        elif action == 2: # Emergency Alert
            # High reward for alerting if stress is high, penalty if low
            pass

        # Clip values to valid range [0, 1]
        self.state = np.clip([stress, vibration, displacement + (vibration * 0.1)], 0, 1)

        # Reward Logic: Penalize high stress/vibration
        reward = 1.0 - (self.state[0] + self.state[1])
        
        # Termination: Structure fails if stress > 0.9
        terminated = bool(self.state[0] > 0.9)
        truncated = False # Typically for time limits

        return self.state, reward, terminated, truncated, {}

    def render(self):
        if self.render_mode == "human":
            print(f"Current State -> Stress: {self.state[0]:.2f}, Vibration: {self.state[1]:.2f}")