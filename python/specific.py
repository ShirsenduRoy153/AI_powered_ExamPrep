import pandas as pd
import mysql.connector

# Establish a connection to the MySQL database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shirsendu@15",
    database="a3"
)

db_cursor = db_connection.cursor()

# Retrieve values from the database
db_cursor.execute("SELECT linkedlist_priority, stack_priority, queue_priority, tree_priority, graph_priority, hashing_priority, heap_priority, sorting_priority, searching_priority, dynamicprogramming_priority FROM statuses WHERE id = 1")
priority = db_cursor.fetchone()

# Close the database connection
db_cursor.close()
db_connection.close()

data_structure_priority = {
    "linkedlist": priority[0],
    "stack": priority[1],
    "queue": priority[2],
    "tree": priority[3],
    "graph": priority[4],
    "hashing": priority[5],
    "heap": priority[6],
    "sorting": priority[7],
    "searching": priority[8],
    "dynamicprogramming": priority[9]
}

# Establish a connection to the MySQL database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shirsendu@15",
    database="a3"
)

db_cursor = db_connection.cursor()

# Retrieve the subject string from the database
db_cursor.execute("SELECT subject FROM outputs WHERE id = 1")
result = db_cursor.fetchone()

db_cursor.close()
db_connection.close()

# Assuming the result is a comma-separated string of subjects
subjects_string = result[0]
subjects = [subject.strip().lower() for subject in subjects_string.split(', ')]

priorities = []
for subject in subjects:
    cleaned_subject = subject.strip('"')  # Remove any extra characters like double quotes
    priorities.append(data_structure_priority[cleaned_subject])

# Create a DataFrame with the subjects and their adjusted priorities
data = {
    'Subject': subjects,
    'Adjusted Priority': priorities
}

df = pd.DataFrame(data)

# Ensure there are no NaN values and at least one priority is non-zero
df['Adjusted Priority'] = df['Adjusted Priority'].fillna(0)
if df['Adjusted Priority'].sum() == 0:
    raise ValueError("Sum of adjusted priorities is zero, cannot allocate slots.")

total_slots = 12 * 7  # 6 hrs
slots_per_subject = [priority * total_slots / sum(priorities) for priority in priorities]

# Round slots to nearest integer
slots_per_subject = [round(slots) for slots in slots_per_subject]

# Calculate total time for each subject in hours
total_time_per_subject = [(slots / 2) + ((slots % 2) * 0.5) for slots in slots_per_subject]

# Create a new list with total hours for each subject
total_hours_list = total_time_per_subject

# Print the list
print(total_hours_list)

total_hours_list = ', '.join(f'"{item}"' for item in total_hours_list)
print("T I M E S = ", total_hours_list)

# Update the priority in the database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shirsendu@15",
    database="a3"
)

db_cursor = db_connection.cursor()

update_query = f"UPDATE outputs SET time = '{total_hours_list}' WHERE id = 1"
db_cursor.execute(update_query)

db_connection.commit()

db_cursor.close()
db_connection.close()

print("Specific")
print("Specific")
print("Specific")
print("Specific")
print("Specific")
print("Specific")