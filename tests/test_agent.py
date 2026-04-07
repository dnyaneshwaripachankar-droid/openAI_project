from src.agents.simple_agent import SimpleAgent
from gymnasium import spaces

def test_agent_action():
    action_space = spaces.Discrete(4)
    agent = SimpleAgent(action_space)

    state = [0, 0]
    action = agent.select_action(state)

    # Check valid action
    assert action in [0, 1, 2, 3]


def test_agent_multiple_actions():
    action_space = spaces.Discrete(4)
    agent = SimpleAgent(action_space)

    for _ in range(10):
        action = agent.select_action([0, 0])
        assert 0 <= action < 4