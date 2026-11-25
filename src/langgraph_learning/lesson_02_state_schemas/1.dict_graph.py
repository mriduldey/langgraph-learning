from langgraph.graph import END, START, StateGraph


def sort_numbers(state: dict) -> dict:
    print("Entered sort_numbers")
    return {"numbers": sorted(state["numbers"])}


builder = StateGraph(dict)
builder.add_node("sort_numbers", sort_numbers)
builder.add_edge(START, "sort_numbers")
builder.add_edge("sort_numbers", END)
graph = builder.compile()

print(graph.invoke({"numbers": [3, 2, 1]}))  # {'numbers': [1, 2, 3]}

try:
    # Even though "2" is a string here sort_numbers starts running.
    # Only during sorting it will see a string instead of number and it will fail,
    # So dict cant do runtime check for type.
    print(graph.invoke({"numbers": [3, "2", 1]})) 
except TypeError as error:
    print("TypeError:", error)