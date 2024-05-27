import mysql.connector
from decimal import Decimal

# Connect to the database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shirsendu@15",
    database="a3"
)

db_cursor = db_connection.cursor()

# Retrieve values from the database
db_cursor.execute("SELECT linkedlist_priority, stack_priority, queue_priority, tree_priority, graph_priority, hashing_priority, heap_priority, sorting_priority, searching_priority, dynamicprogramming_priority FROM statuses WHERE id = 1")
result = db_cursor.fetchone()

# Close the database connection
db_cursor.close()
db_connection.close()

# Convert database results to floats
result = [float(value) if isinstance(value, Decimal) else value for value in result]

from pulp import LpVariable, LpProblem, lpSum, LpBinary, value, LpMaximize, PULP_CBC_CMD

def find_chains_from_node(dependencies, current_node, visited, current_chain, all_chains):
    visited[current_node] = True
    current_chain.append(current_node)

    if not dependencies[current_node]:
        all_chains.append(current_chain.copy())
    else:
        for dependency in dependencies[current_node]:
            if not visited[dependency]:
                find_chains_from_node(dependencies, dependency, visited, current_chain, all_chains)

    current_chain.pop() # Backtrack
    visited[current_node] = False

def get_chains_from_node(dependencies, start_node):
    all_chains = []
    visited = {node: False for node in dependencies}

    if start_node in dependencies:
        find_chains_from_node(dependencies, start_node, visited, [], all_chains)

    return all_chains

# Example usage
dependencies = {
 "LinkedList": ["Stack", "Queue"],
 "Stack": ["Tree", "Graph"],
 "Queue": ["Hashing", "Heap"],
 "Tree": ["Sorting", "Searching"],
 "Graph": ["Heap", "DynamicProgramming"],
 "Hashing": [],
 "Heap": [],
 "Sorting": [],
 "Searching": [],
 "DynamicProgramming": [],
}

start_node = "LinkedList"
chains = get_chains_from_node(dependencies, start_node)

data_structure_priority = {
    "LinkedList": result[0],
    "Stack": result[1],
    "Queue": result[2],
    "Tree": result[3],
    "Graph": result[4],
    "Hashing": result[5],
    "Heap": result[6],
    "Sorting": result[7],
    "Searching": result[8],
    "DynamicProgramming": result[9]
}

chain_strength = [
    sum(data_structure_priority[topic] for topic in chain)
    for chain in chains
]

topics = list(data_structure_priority.keys())
topic_vars = LpVariable.dicts("Topic", topics, 0, 1, LpBinary)

chain_vars = LpVariable.dicts("Chain", range(len(chains)), 0, 1, LpBinary)

prob = LpProblem("StudyChainOptimization", LpMaximize)

# LIMIT
# LIMIT
# LIMIT
total_strength_limit = 30.0 #LIMIT example
# LIMIT
# LIMIT
# LIMIT

penalty = 1000

# Assign weights
strength_weight = 0.8
topics_weight = 0.2
prob += lpSum(chain_strength[i] * chain_vars[i] for i in range(len(chains))) - penalty * (total_strength_limit - lpSum(chain_strength[i] * chain_vars[i] for i in range(len(chains)))) + strength_weight * lpSum(topic_vars)

for i, chain in enumerate(chains):
    prob += lpSum(topic_vars[topic] for topic in chain) <= chain_vars[i]

prob += lpSum(chain_strength[i] * chain_vars[i] for i in range(len(chains))) <= total_strength_limit

prob.solve(PULP_CBC_CMD(msg=0))

selected_chains = [chains[i] for i, var in enumerate(chain_vars.values()) if value(var) > 0]
print("Selected Chains:", selected_chains)

total_strength = sum(chain_strength[i] for i in range(len(chains)) if value(chain_vars[i]) > 0)
print("Total Strength:", total_strength)

print("Chain Strengths:", chain_strength)

l = []

for i in selected_chains:
    for j in i:
        l.append(j)

l = ', '.join(f'"{item}"' for item in l)
print("I T E M S = ", l)

# Update the priority in the database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shirsendu@15",
    database="a3"
)

db_cursor = db_connection.cursor()

update_query = f"UPDATE outputs SET subject = '{l}' WHERE id = 1"
db_cursor.execute(update_query)

db_connection.commit()

db_cursor.close()
db_connection.close()

print("LPP")
print("LPP")
print("LPP")
print("LPP")
print("LPP")
print("LPP")