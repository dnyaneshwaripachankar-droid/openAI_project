# src/training/__init__.py
"""
Top‑level imports for training modules.

Example:
    from src.training import train_agent, run_evaluation
"""

from typing import Any

# Optional: expose core training functions
# from src.training.trainer import train_agent
# from src.training.evaluator import run_evaluation
# from src.training.logger import setup_logger

# If you only want to keep this as a namespace package:
def __getattr__(name: str) -> Any:
    raise AttributeError(f"module 'src.training' has no attribute '{name}'")


# Optional: package‑level metadata
__all__ = [
    # "train_agent",
    # "run_evaluation",
    # "setup_logger",
]