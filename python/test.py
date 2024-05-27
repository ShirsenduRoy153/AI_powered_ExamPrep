from tabulate import tabulate
import mysql.connector
import json
import sys

def create_timetable(busy_slots_per_day):
    timetable = [["Empty" for _ in range(48)] for _ in range(7)]
    for day, busy_slots in enumerate(busy_slots_per_day):
        for slot in busy_slots:
            timetable[day][slot] = "Busy"
    return timetable

def fill_timetable(timetable, items, total_hours):
    day = 0
    slot_counter = 0
    item_index = 0
    consecutive_counter = 0
    study_counter = 0

    for hours in total_hours:
        slots_needed = int(hours * 2)  # Convert hours to slots (assuming 30 min slots)
        while slots_needed > 0:
            if slot_counter >= 48:
                slot_counter = 0
                day += 1

            if day >= 7:
                print("Warning: Not enough slots available in the timetable for all study hours.")
                return timetable

            if timetable[day][slot_counter] == "Empty":
                if study_counter == 3:
                    timetable[day][slot_counter] = "Rest"
                    study_counter = 0
                else:
                    timetable[day][slot_counter] = items[item_index]
                    slots_needed -= 1
                    consecutive_counter += 1
                    study_counter += 1
                    if consecutive_counter == 2:
                        item_index = (item_index + 1) % len(items)
                        consecutive_counter = 0

            slot_counter += 1

        # Add a rest slot after every set of study hours
        if study_counter == 3:
            slot_counter += 1
            if slot_counter >= 48:
                slot_counter = 0
                day += 1
            study_counter = 0

    return timetable

def convert_to_busy_slots(user_input):
    modified_str = user_input.replace('null', '[]')
    busy_slots_per_day = json.loads(modified_str)
    return busy_slots_per_day

# Read user input from command-line argument
user_input = sys.argv[1]
busy_slots_per_day = convert_to_busy_slots(user_input)
timetable = create_timetable(busy_slots_per_day)

# Establish a connection to the MySQL database
db_connection = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Shirsendu@15",
    database="a3"
)

db_cursor = db_connection.cursor()

# Retrieve the subject string from the database
db_cursor.execute("SELECT subject, time FROM outputs WHERE id = 1")
result = db_cursor.fetchone()

db_cursor.close()
db_connection.close()

# String inputs
subjects_input = result[0]
hours_input = result[1]

# Convert string inputs to lists
items = [s.strip().strip('"') for s in subjects_input.split(',')]
total_hours = [float(h.strip().strip('"')) for h in hours_input.split(',')]

timetable_filled = fill_timetable(timetable, items, total_hours)

# Print the timetable in a plain, unformatted way
flat_timetable = [slot for day in timetable_filled for slot in day]
print(" ".join(flat_timetable))