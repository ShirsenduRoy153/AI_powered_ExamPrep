import networkx as nx
import matplotlib.pyplot as plt

nodes = {
    'Node1': 90,
    'Node2': 85,
    'Node3': 80,
    'Node4': 75,
    'Node5': 70,
    'Node6': 65,
    'Node7': 60,
    'Node8': 55,
}

dependencies = {
    'Node1': ['Node2', 'Node3'],
    'Node2': ['Node4', 'Node5'],
    'Node3': ['Node6', 'Node7'],
    'Node4': ['Node8'],
    'Node5': [],
    'Node6': [],
    'Node7': [],
    'Node8': [],
}

G = nx.DiGraph()

for node, mark in nodes.items():
    G.add_node(node, mark=mark)

for node, dependent_nodes in dependencies.items():
    for dependent_node in dependent_nodes:
        G.add_edge(node, dependent_node)

pos = nx.circular_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000, node_color='skyblue', arrowsize=20)

node_labels = {node: f"{node}\n{nodes[node]}" for node in nodes}
nx.draw_networkx_labels(G, pos, labels=node_labels)

plt.show()

def dfs_traversal(current_node, visited):
    print(f"Currently in {current_node} with marks: {nodes[current_node]}")
    visited.add(current_node)

    neighbors = sorted(G.neighbors(current_node), key=lambda node: nodes[node])

    for neighbor in neighbors:
        if neighbor not in visited:
            dfs_traversal(neighbor, visited)

start_node = 'Node1'
dfs_traversal(start_node, set())
