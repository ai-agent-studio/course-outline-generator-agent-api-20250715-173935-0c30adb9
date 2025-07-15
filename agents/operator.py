from enum import Enum
from typing import List, Optional

from agents.agent import course_outline_generator_agent

class AgentType(Enum):
    AGENT = "course_outline_generator"

def get_available_agents() -> List[str]:
    """Returns a list of all available agent IDs."""
    return [agent.value for agent in AgentType]

def get_agent(
    model_id: str = "gpt-4o",
    agent_id: Optional[AgentType] = None,
    user_id: Optional[str] = None,
    session_id: Optional[str] = None,
    debug_mode: bool = True,
):
    if agent_id == AgentType.AGENT or agent_id is None:
        return course_outline_generator_agent(user_id=user_id, session_id=session_id, debug_mode=debug_mode)
    raise ValueError(f"Unknown agent_id: {agent_id}")
