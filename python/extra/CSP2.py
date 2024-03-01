import random

def generate_timetable(subject_code,  priority):
    # Define the domain for each variable
    slots_per_day = 6
    days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
    
    # Randomly assign a day and slot
    day = random.choice(days)
    slot = random.randint(1, slots_per_day)
    
    return {'day': day, 'slot': slot, 'subject_code': subject_code,  'priority': priority}

# Updated input data for 10 subjects
subjects = ["Linked List", "Stack", "Queue", "Tree", "Graph",
            "Hashing", "Heap", "Sorting", "Searching", "Dynamic Programming"]

input_data = [
    (subjects[0], 0.8), (subjects[1], 4), (subjects[2], 2.5), (subjects[3], 1), (subjects[4], 3),
    (subjects[0], 2), (subjects[6], 5), (subjects[7], 4.5), (subjects[8], 2), (subjects[9], 5),
    (subjects[0], 0.9), (subjects[1], 4), (subjects[2], 2.3), (subjects[3], 1.5), (subjects[4], 3),
    (subjects[0], 6), (subjects[6], 5), (subjects[7], 4.7), (subjects[8], 2), (subjects[9], 1),
    (subjects[0], 5), (subjects[1], 4), (subjects[2], 2.3), (subjects[3], 1), (subjects[4], 3),
    (subjects[0], 2), (subjects[6], 5), (subjects[7], 4), (subjects[8], 2), (subjects[9], 1)
]

# Sort input_data by priority
input_data.sort(key=lambda x: x[1], reverse=True)

# Generate timetable for each input
timetable = []
for i, (subject_code,  priority) in enumerate(input_data, start=1):
    solution = generate_timetable(subject_code,  priority)
    timetable.append(solution)

# Assign subjects to days in a well-balanced manner
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
day_index = 0

for slot_info in timetable:
    slot_info['day'] = days[day_index]
    day_index = (day_index + 1) % len(days)

# Print the final timetable
for i, slot_info in enumerate(timetable, start=1):
    print(f"Slot {i}: {slot_info}")
