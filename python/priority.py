import pandas as pd
import math
import mysql.connector

# Connect to the MySQL database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shirsendu@15",
    database="a3"
)

db_cursor = db_connection.cursor()

# Retrieve values from the database
db_cursor.execute("SELECT linkedlist, stack, queue, tree, graph, hashing, heap, sorting, searching, dynamicprogramming, linkedlist_time, stack_time, queue_time, tree_time, graph_time, hashing_time, heap_time, sorting_time, searching_time, dynamicprogramming_time, linkedlist_rating, stack_rating, queue_rating, tree_rating, graph_rating, hashing_rating, heap_rating, sorting_rating, searching_rating, dynamicprogramming_rating FROM statuses WHERE id = 1")
result = db_cursor.fetchone()

# Close the database connection
db_cursor.close()
db_connection.close()

# Define your subject details
subject_details = {
    'LinkedList': {'pre_priority': 2, 'difficulty': 'medium'},
    'Stack': {'pre_priority': 3, 'difficulty': 'hard'},
    'Queue': {'pre_priority': 1, 'difficulty': 'easy'},
    'Tree': {'pre_priority': 2, 'difficulty': 'medium'},
    'Graph': {'pre_priority': 5, 'difficulty': 'hard'},
    'Hashing': {'pre_priority': 3, 'difficulty': 'medium'},
    'Heap': {'pre_priority': 2, 'difficulty': 'hard'},
    'Sorting': {'pre_priority': 4, 'difficulty': 'medium'},
    'Searching': {'pre_priority': 2, 'difficulty': 'medium'},
    'DynamicProgramming': {'pre_priority': 1, 'difficulty': 'easy'}
}

# Define your user data using the retrieved values
user_data = {
    'LinkedList': {'score': result[0], 'rating': result[20], 'time': float(result[10])}, 
    'Stack': {'score': result[1], 'rating': result[21], 'time': float(result[11])},
    'Queue': {'score': result[2], 'rating': result[22], 'time': float(result[12])},
    'Tree': {'score': result[3], 'rating': result[23], 'time': float(result[13])},
    'Graph': {'score': result[4], 'rating': result[24], 'time': float(result[14])},
    'Hashing': {'score': result[5], 'rating': result[25], 'time': float(result[15])},
    'Heap': {'score': result[6], 'rating': result[26], 'time': float(result[16])},
    'Sorting': {'score': result[7], 'rating': result[27], 'time': float(result[17])},
    'Searching': {'score': result[8], 'rating': result[28], 'time': float(result[18])},
    'DynamicProgramming': {'score': result[9], 'rating': result[29], 'time': float(result[19])}
}

data = []

for subject, details in subject_details.items():
    pre_priority = details['pre_priority']
    difficulty = details['difficulty']
    score_concentration = user_data[subject]['score']
    rating = user_data[subject]['rating']
    time = user_data[subject]['time']
    
    # Adjust pre_priority based on difficulty
    if difficulty == 'hard':
        pre_priority += 1
    elif difficulty == 'medium':
        pre_priority += 0.75
    elif difficulty == 'easy':
        pre_priority += 0.5

    pre_priority_weight = 0.25
    score_weight = 1
    rating_weight = 0.5
    time_weight = 0.1

    max_pre_priority = 5
    max_score = 5
    max_rating = 5
    max_time = 10

    personal_priority = (
        pre_priority_weight * (1 - pre_priority / max_pre_priority)+
        score_weight * (1 - score_concentration / max_score) +
        rating_weight * (1 - rating / max_rating) +
        time_weight * (1 - time / max_time)
    )

    personal_priority = 5 / (1 + math.exp(-personal_priority))
    
    if(rating == 0):
        priority_value = round(0.0, 3)
    else:
        priority_value = round(personal_priority, 3)

    # Update the priority in the database
    db_connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password="Shirsendu@15",
        database="a3"
    )

    db_cursor = db_connection.cursor()
    
    update_query = f"UPDATE statuses SET {subject.lower()}_priority = {priority_value} WHERE id = 1"
    db_cursor.execute(update_query)
    
    db_connection.commit()
    
    db_cursor.close()
    db_connection.close()

    data.append([subject, priority_value])

table = pd.DataFrame(data, columns=['Subject', 'Personal Priority'])

print(table)