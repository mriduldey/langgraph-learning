from typing import NotRequired, TypedDict
from langgraph.graph import END, START, StateGraph

# Define state that will be shared throughout the graph
class GraphState(TypedDict):
    """Define the state shared across graph nodes."""
    
    text: str
    result: NotRequired[str]

def format_text(state: GraphState) -> dict[str, str]:
    """ Convert the input text to uppercase."""
    
    return {"result": state["text"].upper() }

# 1.Create graph builderwith store schema
builder = StateGraph(GraphState)

# 2.Register the function as a node
builder.add_node("format_text", format_text)

# 3.Define the execusion path
builder.add_edge(START, "format_text")
builder.add_edge("format_text", END)

# 4. Compile the graph into an executable object
graph = builder.compile()

# Optional -> View graph
graph.get_graph().draw_mermaid_png(
    output_file_path="src\\langgraph_learning\\lesson_01_fundamentals\\state_update_langgraph.png"
)

# 5. Execute the graph using the initial stage
result = graph.invoke({"text": "Hello Ira"})

print(result)
