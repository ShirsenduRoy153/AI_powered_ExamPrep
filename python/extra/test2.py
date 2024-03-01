import random

# Given dependencies
dependencies = {
    'LinkedList': ['Stack', 'Queue'],
    'Stack': ['Tree', 'Graph'],
    'Queue': ['Hashing', 'Heap'],
    'Tree': ['Sorting', 'Searching'],
    'Graph': ['Heap', 'DynamicProgramming'],
    'Hashing': [],
    'Heap': [],
    'Sorting': [],
    'Searching': [],
    'DynamicProgramming': [],
}

# Function to ask for marks
def ask_for_marks(node):
    print(f"Enter marks for {node}: ")
    marks = int(input())
    return marks

# Function to traverse the graph
def traverse_graph(start_node):
    current_node = start_node

    while current_node != 'DynamicProgramming':
        marks = ask_for_marks(current_node)

        # Simulating a pass/fail scenario based on random chance
        if random.random() < marks / 100:
            print(f"Congratulations! You passed {current_node}. Moving to the next node.\n")
            current_node = random.choice(dependencies[current_node] + [current_node])
        else:
            print(f"Oops! You did not pass {current_node}. Going back to the previous node.\n")
            current_node = random.choice([start_node] + dependencies[current_node])

# Start traversal from 'LinkedList'
traverse_graph('LinkedList')

print("Reached DynamicProgramming. Path traversal complete.")
