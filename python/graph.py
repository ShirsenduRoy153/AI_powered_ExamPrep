import sys
import mysql.connector
import networkx as nx
import matplotlib.pyplot as plt

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Shirsendu@15',
    'database': 'a3'
}

db_cursor = None

try:
    db_conn = mysql.connector.connect(**db_config)
    print("MySQL Connection Established")
    db_cursor = db_conn.cursor()

    db_cursor.execute("SELECT linkedlist,stack,queue,tree,graph,hashing,heap,sorting,searching,dyanamicprograming FROM statuses WHERE id = 1")
    result = db_cursor.fetchone()

    topic = sys.argv[1]
    marks = sys.argv[2]
    marks = int(marks)
    marks_threshold = 3

    print("TOPIC IN LOWER CASE : " , topic.lower())

    query = f"UPDATE statuses SET {topic.lower()} = %s, currenttopic = %s, currentscore = %s WHERE id = 1"

    values = (marks, topic, marks)
    db_cursor.execute(query, values)
    db_conn.commit()

    print(f"Updated {topic.lower()} to: {marks}, currenttopic to: {topic}, and currentscore to: {marks}")



    nodes = {
        'LinkedList': result[0],
        'Stack': result[1],
        'Queue': result[2],
        'Tree': result[3],
        'Graph': result[4],
        'Hashing': result[5],
        'Heap': result[6],
        'Sorting': result[7],
        'Searching': result[8],
        'DynamicProgramming': result[9],
    }

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

    for node in nodes:
        if node == topic:
            nodes[node] = marks

    G = nx.DiGraph()

    for node, mark in nodes.items():
        G.add_node(node, mark=mark)

    for node, dependent_nodes in dependencies.items():
        for dependent_node in dependent_nodes:
            G.add_edge(node, dependent_node)

    pos = nx.circular_layout(G)
    nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=2000, node_color='skyblue', arrowsize=20)

    node_labels = {node: f"{node}" for node in nodes}
    nx.draw_networkx_labels(G, pos, labels=node_labels)

    plt.show()

    def dfs_traversal(graph, current_node, visited, traversal_list, marks_threshold):
        node_info = {'name': current_node, 'marks': graph.nodes[current_node]['mark']}
        traversal_list.append(node_info)
        visited.add(current_node)

        if node_info['marks'] >= marks_threshold:
            neighbors = sorted(graph.neighbors(current_node), key=lambda node: graph.nodes[node]['mark'])

            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs_traversal(graph, neighbor, visited, traversal_list, marks_threshold)

    start_node = 'LinkedList'
    traversal_result = []
    dfs_traversal(G, start_node, set(), traversal_result, marks_threshold)

    for node_info in traversal_result:
        if node_info['marks'] < marks_threshold:
            print(f"Name: {node_info['name']}, Marks: {node_info['marks']}")
            query = "UPDATE `a3`.`statuses` SET `currenttopic` = %s, `currentscore` = %s WHERE `id` = 1"
            #eai currenttopic er subject tar marks o change korte hobe borohate naki choto haate lekha seita dekhte hobr
            values = (node_info['name'], node_info['marks'])
            db_cursor.execute(query, values)
            db_conn.commit()
            break

# except mysql.connector.Error as err:
#     print(f"Error: {err}")
#     sys.exit(1)

finally:
    if db_cursor:
        db_cursor.close()
    if db_conn.is_connected():
        db_conn.close()