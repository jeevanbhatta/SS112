import matplotlib.pyplot as plt
import networkx as nx

# Define the nodes and edges for the Causal Loop Diagram
# Nodes represent variables in the system
# Using newlines to wrap text inside nodes
nodes = [
    "Corruption", 
    "Economic\nStagnation", 
    "Youth Migration\n(Exit)", 
    "Remittances", 
    "Govt Revenue\n(Import Tax)", 
    "Pressure\nfor Reform", 
    "Digital\nConnectivity", 
    "Awareness\nof Scandals", 
    "Public\nMobilization\n(Voice)", 
    "State\nRepression"
]

# Edges represent causal links
# (Source, Target, Type) where Type is '+' (Reinforcing) or '-' (Balancing)
edges = [
    ("Corruption", "Economic\nStagnation", "+"),
    ("Economic\nStagnation", "Youth Migration\n(Exit)", "+"),
    ("Youth Migration\n(Exit)", "Remittances", "+"),
    ("Remittances", "Govt Revenue\n(Import Tax)", "+"),
    ("Govt Revenue\n(Import Tax)", "Pressure\nfor Reform", "-"), # Remittances buffer the state, reducing need for reform
    ("Pressure\nfor Reform", "Corruption", "-"), # Less pressure allows corruption to continue
    
    # The Disruption Loop (Gen Z)
    ("Corruption", "Awareness\nof Scandals", "+"),
    ("Digital\nConnectivity", "Awareness\nof Scandals", "+"),
    ("Awareness\nof Scandals", "Public\nMobilization\n(Voice)", "+"),
    ("Public\nMobilization\n(Voice)", "Pressure\nfor Reform", "+"),
    
    # The Conflict Loop
    ("Public\nMobilization\n(Voice)", "State\nRepression", "+"),
    ("State\nRepression", "Public\nMobilization\n(Voice)", "+"), # Backfire effect (Reinforcing loop of conflict)
]

# Create the graph
G = nx.DiGraph()
G.add_nodes_from(nodes)
for u, v, t in edges:
    G.add_edge(u, v, type=t)

# Layout
pos = {
    "Corruption": (0, 1),
    "Economic\nStagnation": (-1, 0.5),
    "Youth Migration\n(Exit)": (-1, -0.5),
    "Remittances": (0, -1),
    "Govt Revenue\n(Import Tax)": (1, -0.5),
    "Pressure\nfor Reform": (1, 0.5),
    
    "Digital\nConnectivity": (2, 1.5),
    "Awareness\nof Scandals": (2, 0.5),
    "Public\nMobilization\n(Voice)": (3, 0),
    "State\nRepression": (3, -1)
}

# Draw
plt.figure(figsize=(14, 8))

# Draw nodes
# Increased node size slightly to accommodate wrapped text
node_size = 3500
nx.draw_networkx_nodes(G, pos, node_size=node_size, node_color='lightblue', edgecolors='black')
nx.draw_networkx_labels(G, pos, font_size=8, font_weight='bold')

# Draw edges
for u, v, d in G.edges(data=True):
    style = 'solid'
    color = 'green' if d['type'] == '+' else 'red'
    
    # Curved edges to avoid overlap
    connection_style = "arc3,rad=0.1"
    
    # Explicitly setting arrows=True and arrowstyle
    # IMPORTANT: Must pass node_size so edges stop at the node boundary, not the center
    nx.draw_networkx_edges(G, pos, edgelist=[(u, v)], edge_color=color, 
                           style=style, width=2, 
                           arrows=True, arrowsize=20, arrowstyle='-|>',
                           node_size=node_size,
                           connectionstyle=connection_style)

# Annotate Loops
plt.text(0, 0, "Remittance Trap\n(Balancing Loop)", ha='center', fontsize=12, fontweight='bold', color='red', bbox=dict(facecolor='white', alpha=0.8))
# Moved Protest Cycle caption to avoid overlap with edges (Awareness -> Mobilization)
plt.text(3.2, 0.8, "Protest Cycle\n(Reinforcing Loop)", ha='center', fontsize=12, fontweight='bold', color='green', bbox=dict(facecolor='white', alpha=0.8))

plt.title("Complex Causality of Nepal's Political Unrest", fontsize=16)
plt.axis('off')

# Legend
from matplotlib.lines import Line2D
legend_elements = [
    Line2D([0], [0], color='green', lw=2, label='Positive Link (+)'),
    Line2D([0], [0], color='red', lw=2, label='Negative Link (-)')
]
plt.legend(handles=legend_elements, loc='upper right')

plt.tight_layout()
plt.savefig("nepal_complex_causality.png")
print("Saved nepal_complex_causality.png")
