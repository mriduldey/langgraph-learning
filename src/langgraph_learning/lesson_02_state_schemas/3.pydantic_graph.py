# Here we will see that invokation itself failing when type is mismatching.

from langgraph.graph import END, START, StateGraph
from pydantic import BaseModel, ConfigDict, ValidationError


class SortState(BaseModel):
    model_config = ConfigDict(strict=True)
    numbers: list[int]


def sort_numbers(state: SortState) -> dict[str, list[int]]:
    print("Entered sort_numbers")
    return {"numbers": sorted(state.numbers)}


builder = StateGraph(SortState)
builder.add_node("sort_numbers", sort_numbers)
builder.add_edge(START, "sort_numbers")
builder.add_edge("sort_numbers", END)
graph = builder.compile()

print(graph.invoke({"numbers": [3, 2, 1]}))  # {'numbers': [1, 2, 3]}

try:
    print(graph.invoke({"numbers": [3, "2", 1]}))
except ValidationError as error:
    for detail in error.errors():
        print(detail["loc"], detail["msg"])
        # ('numbers', 1) Input should be a valid integer