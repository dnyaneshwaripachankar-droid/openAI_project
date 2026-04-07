"""
OpenEnv Client for Structural Safety Twin
Usage: 
    client = StructuralClient(url="http://localhost:8000")
    obs = client.reset()
"""

from openenv import EnvClient
from types import YourAction, YourObservation, YourState

class StructuralClient(EnvClient[YourAction, YourObservation, YourState]):
    """
    Typed client for interacting with the Structural Safety environment.
    """
    def __init__(self, url: str = "http://localhost:8000", **kwargs):
        # EnvClient handles the HTTP/WebSocket connection logic
        super().__init__(
            url=url,
            action_type=YourAction,
            observation_type=YourObservation,
            state_type=YourState,
            **kwargs
        )

    def get_safety_status(self) -> str:
        """Example of a helper method to interpret observations."""
        if self.last_observation and self.last_observation.sensors[0] > 0.7:
            return "DANGER: HIGH STRESS"
        return "SAFE"

if __name__ == "__main__":
    # Quick Test: Connect and take one step
    with StructuralClient() as client:
        obs = client.reset()
        print(f"Initial Sensors: {obs.sensors}")
        
        # Take a 'Do Nothing' action
        new_obs, reward, done, info = client.step(YourAction(action_id=0))
        print(f"Reward: {reward} | Done: {done}")