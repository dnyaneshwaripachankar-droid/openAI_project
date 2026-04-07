import numpy as np
from typing import Tuple, Dict, Any
from openenv import Environment
from .types import YourAction, YourObservation, YourState

class YourEnvironment(Environment[YourAction, YourObservation, YourState]):
    """
    Smart Digital Twin for Structural Health Monitoring.
    Simulates stress, vibration, and displacement for safety assessment.
    """

    def __init__(self):
        super().__init__()
        # Initial ground truth state
        self._state = YourState(
            stress=0.1,
            vibration=0.2,
            displacement=0.05,
            fatigue_index=0.0,
            step_count=0
        )

    def reset(self, seed: int | None = None) -> Tuple[YourObservation, Dict[str, Any]]:
        """Resets the building to a baseline 'Healthy' state."""
        self._state = YourState(
            stress=0.1,
            vibration=0.2,
            displacement=0.05,
            fatigue_index=0.0,
            step_count=0
        )
        
        observation = self.state_to_observation(self._state)
        return observation, {"status": "Structure Reset: Baseline healthy"}

    def step(self, action: YourAction) -> Tuple[YourObservation, float, bool, bool, Dict[str, Any]]:
        """Applies an intervention and calculates structural response."""
        s = self._state
        s.step_count += 1

        # 1. Natural Dynamics (Wind/Traffic Load)
        load_surge = np.random.normal(0.02, 0.01)
        s.stress += load_surge
        s.vibration += np.random.normal(0.01, 0.005)

        # 2. Apply Agent Intervention
        if action.action_id == 1:  # Active Damping
            s.vibration *= 0.5
            s.stress -= 0.01
        elif action.action_id == 2: # Emergency Lockdown
            s.stress *= 0.8
            s.vibration = 0.02

        # 3. Update Displacement & Fatigue
        s.displacement = np.clip(s.displacement + (s.vibration * 0.1), 0, 1)
        s.fatigue_index += (s.stress * 0.001)

        # 4. Reward Logic (High reward for stability, heavy penalty for failure)
        reward = 1.0 - (s.stress + s.vibration)
        
        # 5. Termination (Structure Fails if stress > 0.9)
        terminated = bool(s.stress > 0.9)
        truncated = bool(s.step_count >= 500)

        observation = self.state_to_observation(s)
        return observation, float(reward), terminated, truncated, {}

    def state_to_observation(self, state: YourState) -> YourObservation:
        """Converts internal 'Ground Truth' to what the Agent sees."""
        # Adding 'sensor noise' to make the agent more robust
        noise = np.random.normal(0, 0.005, size=3)
        raw_sensors = np.array([state.stress, state.vibration, state.displacement])
        return YourObservation(sensors=np.clip(raw_sensors + noise, 0, 1))

    @property
    def state(self) -> YourState:
        """Returns the current full internal state."""
        return self._state