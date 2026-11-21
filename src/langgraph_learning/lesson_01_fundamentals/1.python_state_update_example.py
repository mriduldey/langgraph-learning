from typing import Any


def format_text(state: dict) -> dict:
    """Convert the input text to uppercase."""
    return {"result": state["text"].upper()} # 1


state: dict[str, Any] = {"text": "Hello LangGraph"}

update = format_text(state)

state.update(update) # 2

print("Updated state: ", state)

print("-----------------------------------------------------")

# The function returns only the changed data [1], and Python merges that change into the existing dictionary [2].
# This is very similar to the state-update pattern used by LangGraph.

# What happens When the workflow grows?


def validate_text(state):
    return {"valid": bool(state["text"].strip())}

state: dict[str, Any] = {"text": "Hello Ira"}

state.update(validate_text(state))

if state["valid"]:
    state.update(format_text(state))
    
print("Updated state: ", state);

# However, as the workflow grows, you must maintain the control flow, select the next function, and merge the updates yourself.
# LangGraph provides a structured way to define these operations and execute them consistently.