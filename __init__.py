"""
OpenEnv Structural Safety Twin
This module exports the core classes required for the RL training loop.
"""

from .environment import YourEnv
from types import YourAction, YourObservation

# Ensure these are accessible at the package level
__all__ = [
    "YourEnv",
    "YourAction",
    "YourObservation",
]

# Metadata for version tracking
__version__ = "1.0.0"

# Optional: Register the environment with Gymnasium if using local testing
try:
    from gymnasium.envs.registration import register
    
    register(
        id="OpenEnv/StructuralSafety-v0",
        entry_point="server.environment:YourEnv",
        max_episode_steps=1000,
        reward_threshold=100.0,
    )
except ImportError:
    # Fail silently if gymnasium is not installed in the current context
    pass