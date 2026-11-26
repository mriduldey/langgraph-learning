state = {
    "text": "Hello",
    "logs": ["Started"]
}

update = {
    "logs": ["Text normalized"]
}

def merge_logs(existing: list[str], incoming: list[str]):
    """Combine existing and incoming logs."""
    return existing + incoming


state["logs"] = merge_logs(state["logs"], update["logs"]);

print(state);