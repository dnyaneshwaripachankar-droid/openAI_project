from dataclasses import dataclass
import numpy as np
from openai_env.core.schema import Action, Observation, State

@dataclass
class YourAction(Action):
    """
    Defines the available interventions for the structural twin.
    0: Monitor Only (No action)
    1: Activate Dampers (Reduce vibration)
    2: Emergency Lockdown (Stop all operations)
    """
    action_id: int

@dataclass
class YourObservation(Observation):
    """
    The sensor data bundle passed to the agent at each step.
    Expected shape: [stress, vibration, displacement]
    """
    sensors: np.ndarray

@dataclass
class YourState(State):
    """
    The internal 'ground truth' of the simulation.
    Includes hidden variables like material fatigue or temperature 
    that might not be fully visible in the observation.
    """
    stress: float
    vibration: float
    displacement: float
    fatigue_index: float
    step_count: int