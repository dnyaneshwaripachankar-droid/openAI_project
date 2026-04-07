# my_env/models.py
from openai_env.core.schema import Action, Observation, State
from pydantic import BaseModel, Field

class MyAction(Action, BaseModel):
    chosen_column: int = Field(..., ge=0, lt=7, description="Which column to drop the piece (0–6)")

class MyObservation(Observation, BaseModel):
    board: list[list[str | None]] = Field(..., description="4×4 grid of X/O/None")
    legal_actions: list[int] = Field(..., description="Columns where a move is allowed")
    done: bool = Field(..., description="Is the game over?")

class MyState(State, BaseModel):
    board: list[list[str | None]]
    next_player: str
    moves: int
    episode_id: str
    step_count: int