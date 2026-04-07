from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Any, Dict

# Internal imports from your project structure
from server.environment import YourEnv
from server.types import YourAction, YourObservation, YourState

app = FastAPI(title="Structural Safety OpenEnv Server")

# Initialize the environment globally (or per-session in a real hackathon)
env = YourEnv()

@app.get("/health")
def health_check():
    """Confirms the server is running and the environment is loaded."""
    return {"status": "healthy", "env": "structural-safety-v0"}

@app.get("/spec")
def get_spec():
    """Returns the observation and action space metadata."""
    return {
        "action_space": str(env.action_space),
        "observation_space": str(env.observation_space),
        "render_modes": env.metadata["render_modes"]
    }

@app.post("/reset")
def reset_env():
    """Resets the twin to the initial state."""
    obs, info = env.reset()
    return {"observation": obs.tolist(), "info": info}

@app.post("/step")
def step_env(action: YourAction):
    """Executes an action and returns the transition data."""
    try:
        obs, reward, terminated, truncated, info = env.step(action.action_id)
        return {
            "observation": obs.tolist(),
            "reward": float(reward),
            "terminated": terminated,
            "truncated": truncated,
            "info": info
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))

@app.get("/state")
def get_state():
    """Returns the 'ground truth' state (YourState) for debugging/eval."""
    # Mapping current internal env state to the YourState schema
    current_state = YourState(
        stress=float(env.state[0]),
        vibration=float(env.state[1]),
        displacement=float(env.state[2]),
        fatigue_index=0.01, # Example hidden variable
        step_count=0
    )
    return current_state