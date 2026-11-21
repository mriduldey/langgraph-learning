from typing import NotRequired, TypedDict
from langgraph.graph import START, END, StateGraph

class GraphState(TypedDict):
    """Define the shared graph state."""
    
    text: str
    result: NotRequired[str]
    length: NotRequired[int]

def normalize_text(state: GraphState) -> dict[str, str]:
    """Remove surrounding whitespace."""
    
    return {"text": state["text"].strip()}

def format_text(state: GraphState) -> dict[str, str]:
    """Convert text to uppercase."""
    
    return {"result": state["text"].upper()}

def count_char(state: GraphState) -> dict[str, int]:
    """Count characters in the processed text."""
    
    return {"length": len(state["text"])}

# Create builder
builder = StateGraph(GraphState)

# Register nodes | note: By default builder adds key
builder.add_node(normalize_text)
builder.add_node(format_text)
builder.add_node(count_char)

# Define the edges
builder.add_edge(START, "normalize_text")
builder.add_edge("normalize_text", "format_text")
builder.add_edge("normalize_text", "count_char")
builder.add_edge("count_char", END)
builder.add_edge("format_text", END)


graph = builder.compile()
# graph.get_graph().draw_mermaid_png(
#     output_file_path="src\\langgraph_learning\\lesson_01_fundamentals\\4.multi_concurrent_node.png"
# )


result = graph.invoke({"text": "  Hello Ira  "})

print(result)