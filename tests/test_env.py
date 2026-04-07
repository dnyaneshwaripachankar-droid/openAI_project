from src.envs.custom_env import CustomEnv

def test_env_initialization():
    config = {
        "environment": {
            "grid_size": 5,
            "goal_position": [4, 4]
        }
    }

    env = CustomEnv(config)
    state, _ = env.reset()

    # Check state shape
    assert len(state) == 2


def test_env_step():
    config = {
        "environment": {
            "grid_size": 5,
            "goal_position": [4, 4]
        }
    }

    env = CustomEnv(config)
    state, _ = env.reset()

    action = 3  # move right
    next_state, reward, done, _, _ = env.step(action)

    # Check state update
    assert len(next_state) == 2

    # Reward should be numeric
    assert isinstance(reward, (int, float))