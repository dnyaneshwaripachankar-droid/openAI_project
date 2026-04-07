from dataclasses import dataclass
import numpy as np
from openenv import Action, Observation, State

@dataclass
class YourAction(Action):
    """
    Interventions available to the structural agent.
    0: Passive Monitoring
    1: Active Damping (Reduces vibration/oscillation)
    2: Emergency Lockdown (Closes building/stops loads)
    """
    action_id: int

@dataclass
class YourObservation(Observation):
    """
    The data provided to the AI agent's policy.
    Represents noisy or partial sensor readings.
    """
    sensors: np.ndarray  # [stress_obs, vib_obs, disp_obs]

@dataclass
class YourState(State):
    """
    The 'Ground Truth' used by the simulator.
    Includes hidden variables not directly visible to the agent.
    """
    stress: float
    vibration: float
    displacement: float
    fatigue_index: float  # Hidden variable determining structural health
    step_count: int