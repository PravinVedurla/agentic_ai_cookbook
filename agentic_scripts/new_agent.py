# Add Graphviz import for visualization
from graphviz import Digraph
from IPython.display import Image, display
# Import required libraries
from langgraph.graph import StateGraph, END
from langchain_core.runnables import RunnableLambda

# Define a basic state class to represent the agent's memory/state
class AgentState(dict):
    pass  # Can extend with specific properties later

# Define a simple function the agent will perform
def greet(state: AgentState) -> AgentState:
    print("Hello! I am a basic LangGraph agent.")
    return state  # return the state unchanged

def farewell(state: AgentState) -> AgentState:
    print("Goodbye! The agent has completed its task.")
    return state

# Create a state graph to define the flow of the agent
graph_builder = StateGraph(AgentState)

# Add a node to the graph. The node is a task (function) to be run.
graph_builder.add_node("greet_node", RunnableLambda(greet))
graph_builder.add_node("farewell_node", RunnableLambda(farewell))

# Set the entry point of the graph
graph_builder.set_entry_point("greet_node")

# Set the next step after greet_node to farewell_node
graph_builder.add_edge("greet_node", "farewell_node")
graph_builder.add_edge("farewell_node", END)
# graph_builder.add_edge("greet_node", END)

# Compile the graph into a runnable object
graph = graph_builder.compile()


# Function to visualize the graph using Graphviz
def visualize_graph():
    dot = Digraph()

    # Add nodes
    dot.node("greet_node", "Greet Node")
    dot.node("farewell_node", "Farewell Node")
    dot.node("END", "End")

    # Add edges
    dot.edge("greet_node", "farewell_node")
    dot.edge("farewell_node", "END")

    # Render the diagram to a file
    filepath = dot.render("agent_graph", format="png", cleanup=True)
    display(Image(filename=filepath))

visualize_graph()

# Execute the agent with an initial state (empty for now)
graph.invoke(AgentState())
