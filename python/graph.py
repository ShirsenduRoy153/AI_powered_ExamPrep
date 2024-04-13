import sys
import mysql.connector
import networkx as nx

db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'Shirsendu@15',
    'database': 'a3'
}

try:
    db_conn = mysql.connector.connect(**db_config)
    print("MySQL Connection Established")
    db_cursor = db_conn.cursor()

    db_cursor.execute("SELECT linkedlist,stack,queue,tree,graph,hashing,heap,sorting,searching,dynamicprogramming FROM statuses WHERE id = 1")
    result = db_cursor.fetchone()

    topic = sys.argv[1]
    marks = sys.argv[2]
    marks = int(marks)
    marks_threshold = 3

    print("TOPIC IN LOWER CASE : ", topic.lower())

    # Collect updates in a list
    updates = []
    
    query = f"UPDATE statuses SET {topic.lower()} = %s, currenttopic = %s, currentscore = %s WHERE id = 1"
    values = (marks, topic, marks)
    updates.append((query, values))

    nodes = {
        'linkedlist': result[0],
        'stack': result[1],
        'queue': result[2],
        'tree': result[3],
        'graph': result[4],
        'hashing': result[5],
        'heap': result[6],
        'sorting': result[7],
        'searching': result[8],
        'dynamicprogramming': result[9],
    }

    dependencies = {
        'linkedlist': ['stack', 'queue'],
        'stack': ['tree', 'graph'],
        'queue': ['hashing', 'heap'],
        'tree': ['sorting', 'searching'],
        'graph': ['heap', 'dynamicprogramming'],
        'hashing': [],
        'heap': [],
        'sorting': [],
        'searching': [],
        'dynamicprogramming': [],
    }

    # Create the graph once
    G = nx.DiGraph()

    for node, mark in nodes.items():
        G.add_node(node, mark=mark)

    for node, dependent_nodes in dependencies.items():
        for dependent_node in dependent_nodes:
            G.add_edge(node, dependent_node)

    pos = nx.circular_layout(G)

    def dfs_traversal(graph, current_node, visited, traversal_list, marks_threshold):
        node_info = {'name': current_node, 'marks': graph.nodes[current_node]['mark']}
        traversal_list.append(node_info)
        visited.add(current_node)

        if node_info['marks'] >= marks_threshold:
            neighbors = sorted(graph.neighbors(current_node), key=lambda node: graph.nodes[node]['mark'])

            for neighbor in neighbors:
                if neighbor not in visited:
                    dfs_traversal(graph, neighbor, visited, traversal_list, marks_threshold)

    start_node = 'linkedlist'
    traversal_result = []
    dfs_traversal(G, start_node, set(), traversal_result, marks_threshold)

    for node_info in traversal_result:
        if node_info['marks'] < marks_threshold:
            print(f"Name: {node_info['name']}, Marks: {node_info['marks']}")
            # Collect update in the list
            query = "UPDATE `a3`.`statuses` SET `currenttopic` = %s, `currentscore` = %s WHERE `id` = 1"
            values = (node_info['name'], node_info['marks'])
            updates.append((query, values))
            break

    # Execute all updates in a batch
    for update_query, update_values in updates:
        db_cursor.execute(update_query, update_values)
        db_conn.commit()

finally:
    if db_cursor:
        db_cursor.close()
    if db_conn.is_connected():
        db_conn.close()