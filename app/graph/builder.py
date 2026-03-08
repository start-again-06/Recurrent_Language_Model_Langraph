import logging
from langgraph.graph import StateGraph, END
from graph.state import AgentState
from graph.nodes import agent_node, tools_node_with_logging
from graph.edges import should_continue
from services.memory import get_checkpointer

logger = logging.getLogger("rlm_agent")


_graph = None


def build_graph():
    
    global _graph
    if _graph is not None:
        return _graph

    logger.info("Building LangGraph StateGraph...")

    workflow = StateGraph(AgentState)

    workflow.add_node("agent", agent_node)
    workflow.add_node("tools", tools_node_with_logging)

    workflow.set_entry_point("agent")

   
    workflow.add_conditional_edges(
        "agent",          # from this node
        should_continue,  # call this function to decide
        {
            "tools": "tools",  # if returns "tools" → go to tools node
            "end": END,        # if returns "end"   → stop
        }
    )

   
    workflow.add_edge("tools", "agent")

    checkpointer = get_checkpointer()
    _graph = workflow.compile(checkpointer=checkpointer)

    logger.info("LangGraph StateGraph compiled successfully")
    return _graph
