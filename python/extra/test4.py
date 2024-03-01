import networkx as nx
import numpy as np

# Define the graph structure
G = nx.DiGraph()
G.add_edges_from([
    ("LinkedList", "Stack"),
    ("LinkedList", "Queue"),
    ("Stack", "Tree"),
    ("Stack", "Graph"),
    ("Queue", "Hashing"),
    ("Queue", "Heap"),
    ("Tree", "Sorting"),
    ("Tree", "Searching"),
    ("Graph", "Heap"),
    ("Graph", "DynamicProgramming"),
    ("Sorting", "Algorithms"),
    ("Searching", "Algorithms"),
    ("Hashing", "Data Structures"),
    ("Heap", "Data Structures"),
    ("Algorithms", "None"),
    ("Data Structures", "None")
])

# Initialize marks dictionary with None
marks = {
    "LinkedList": None,
    "Stack": None,
    "Queue": None,
    "Tree": None,
    "Graph": None,
    "Hashing": None,
    "Heap": None,
    "Sorting": None,
    "Searching": None,
    "Algorithms": None,
    "Data Structures": None
}

# State representation
def state_representation(current_subject):
    return current_subject

# Valid actions
def get_valid_actions(G, state):
    return list(G.successors(state))

# Reward function (update based on your requirements)
def reward_function(state, action, next_state, marks):
    current_subject = state
    next_subject = action
    current_mark = marks.get(current_subject, None)

    reward = 0
    if current_mark is not None and current_mark > 33:
        reward += 1  # Positive reward for good mark
    return reward

# Q-learning algorithm outline with user input and backtracking
learning_rate = 0.8
discount_factor = 0.9
epsilon = 0.1

Q = np.zeros((len(G.nodes()), len(G.nodes())))

# Episodes (study sessions) loop
for episode in range(1000):  # Adjust number of episodes for learning
    state = np.random.choice(list(G.nodes()))
    visited_states = []  # Track visited states to avoid loops

    while True:
        # Choose an action (consider visiting only unvisited nodes)
        valid_actions = [a for a in get_valid_actions(G, state) if a not in visited_states]
        if valid_actions:
            if np.random.rand() < epsilon:  # Exploration
                action = np.random.choice(valid_actions)
            else:  # Exploitation
                action = np.argmax(Q[state][valid_actions])
        else:
            # No valid actions (may need adjustments based on your graph structure)
            print("No valid unvisited actions. Skipping iteration.")
            break

        # Take the action
        valid_actions = get_valid_actions(G, state)
        action_index = valid_actions.index(action)

        # Update Q-table using valid index
        Q[state][action_index] = Q[state][action_index] + learning_rate * (reward + discount_factor * np.max(Q[next_state]))


        # User input for mark (replace with appropriate input function)
        current_mark = float(input("Enter your mark for {}: ".format(state)))
        marks[state] = current_mark

        # Observe reward and next state
        reward = reward_function(state, action, action, marks)
        next_state = action

        # Update the Q-table
        Q[state][action] = Q[state][action] + learning_rate * (reward + discount_factor * np.max(Q[next_state]))


        # Backtracking logic
        if current_mark is not None and current_mark < 33:  # Backtrack on low mark
            next_state = state  # Stay in the current state

        # Add state to visited list
        visited_states.append(state)

        # Terminal condition (e.g., all subjects learned well)
        if all(mark > 33 for mark in marks.values() if mark is not None):
            break

        state = next_state

# Agent is ready!
print("Q-table after training:")
print(Q)

# To use the trained agent:
# - Start with an initial subject (e.g., "LinkedList").
# - Use the Q-table to determine the next subject with the highest Q-value
#   (considering only unvisited nodes).
# - Repeat until all subjects are learned well or another stopping criterion is met.
