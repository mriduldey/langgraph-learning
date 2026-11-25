# What we saw for dict still can be seen using TypedDcit.
# But, here the improvement is we can define the expected type. This is helpful for staic type checking
# not runtime

from langgraph.graph import END, START, StateGraph
from typing_extensions import TypedDict


class SortState(TypedDict):
    numbers: list[int]


def sort_numbers(state: SortState) -> SortState:
    print("Entered sort_numbers")
    return {"numbers": sorted(state["numbers"])}


builder = StateGraph(SortState)
builder.add_node("sort_numbers", sort_numbers)
builder.add_edge(START, "sort_numbers")
builder.add_edge("sort_numbers", END)
graph = builder.compile()

print(graph.invoke({"numbers": [3, 2, 1]}))  # {'numbers': [1, 2, 3]}

# Intentional mistake: mypy can flag "2" on this assignment.
bad_input: SortState = {"numbers": [3, "2", 1]}

try:
    print(graph.invoke(bad_input))
except TypeError as error:
    print("TypeError:", error)