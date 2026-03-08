import logging
from langchain_core.messages import AIMessage
from graph.state import AgentState
from core.config import get_settings

logger = logging.getLogger("rlm_agent")


def should_continue(state: AgentState) -> str:
    
    settings = get_settings()
    last_message = state["messages"][-1]
    depth = state.get("recursion_depth", 0)

    
    if depth >= settings.rlm_agent_max_iterations:
        logger.warning(f"[edges] Max iterations ({settings.rlm_agent_max_iterations}) reached, forcing end")
        return "end"

    
    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        logger.info(f"[edges] Routing to tools (depth={depth})")
        return "tools"

    logger.info(f"[edges] Final answer reached (depth={depth})")
    return "end"
