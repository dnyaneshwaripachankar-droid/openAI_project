import gymnasium as gym
import numpy as np
from typing import Tuple, Dict, Any

# Ensure YourAction and YourObservation are defined in your types.py
from  types import YourAction, YourObservation, YourState

class YourEnv(gym.Env):
    """
    Structural Safety Digital Twin Environment.
    The agent must maintain structural integrity by adjusting 
    active damping or triggering maintenance alerts.
    """
    metadata = {"render_modes": ["human", "rgb_array"], "render_fps": 30}

    def __init__(self, render_mode=None):
        super(YourEnv, self).__init__()
        
        # Action Space: 0: No Action, 1: Increase Damping, 2: Emergency Alert
        self.action_space = gym.spaces.Discrete(3)

        # Observation Space: [Normalized Stress, Vibration, Displacement]
        self.observation_space = gym.spaces.Box(
            low=0, high=1, shape=(3,), dtype=np.float32
        )

        self.render_mode = render_mode
        self.state = None
        self.step_count = 0

    def reset(self, seed=None, options=None) -> Tuple[np.ndarray, Dict[str, Any]]:
        """Resets the twin to a safe baseline state."""
        super().reset(seed=seed)
        
        # Baseline sensors: Stress: 10%, Vibration: 20%, Displacement: 5%
        self.state = np.array([0.1, 0.2, 0.05], dtype=np.float32)
        self.step_count = 0
        
        info = {"status": "Structural monitoring active"}
        return self.state, info

    def step(self, action: int) -> Tuple[np.ndarray, float, bool, bool, Dict[str, Any]]:
        """Applies an action and calculates the new physical state."""
        self.step_count += 1
        stress, vibration, displacement = self.state

        # Environmental noise (Simulating wind/traffic loads)
        stress += np.random.normal(0.01, 0.015)
        vibration += np.random.normal(0.005, 0.01)

        # Action Logic
        if action == 1:  # Active Damping
            vibration *= 0.8
            stress -= 0.005
        elif action == 2: # Emergency Alert
            # High immediate safety, but high operational 'cost'
            pass

        # Update Displacement based on vibration and stress
        displacement = np.clip(displacement + (vibration * 0.1), 0, 1)
        self.state = np.clip([stress, vibration, displacement], 0, 1)

        # Reward: High value for low stress/vibration, penalty for failure
        reward = 1.0 - (self.state[0] * 0.6 + self.state[1] * 0.4)
        
        # Termination: Structure fails if stress exceeds 90%
        terminated = bool(self.state[0] > 0.9)
        truncated = bool(self.step_count >= 1000)

        return self.state, reward, terminated, truncated, {}

    def render(self):
        if self.render_mode == "human":
            print(f"Step {self.step_count} | Stress: {self.state[0]:.2f} | Vib: {self.state[1]:.2f}")