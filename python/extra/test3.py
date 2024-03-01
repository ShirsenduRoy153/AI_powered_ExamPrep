# Predefined data (replace with your own if needed)
subjects = ["Math", "Physics", "Chemistry", "History", "Literature"]
priorities = {"Math": "High", "Physics": "Medium", "Chemistry": "Low", "History": "High", "Literature": "Medium"}
marks = {"Math": 70, "Physics": 65, "Chemistry": 80, "History": 55, "Literature": 60}

def calculate_timetable(subjects, priorities, marks, available_time):
    # Replace this with your desired logic for allocating time based on priority and remaining availability.
    # This is a simple example for demonstration purposes.
    time_allocation = {
        "High": 2,
        "Medium": 1.5,
        "Low": 1
    }

    timetable = []
    remaining_time = available_time
    for subject in subjects:
        allocated_time = min(time_allocation[priorities[subject]], remaining_time)
        remaining_time -= allocated_time
        timetable.append({
            "subject": subject,
            "priority": priorities[subject],
            "marks": marks[subject],
            "allocated_time": allocated_time
        })

    return timetable

def print_timetable(timetable):
    # Print header
    print("Subject | Priority | Marks | Time (Hrs)")
    print("------- | -------- | -------- | --------")

    # Print each subject and its details
    for entry in timetable:
        print(f"{entry['subject']:<8} | {entry['priority']:<8} | {entry['marks']:<8.1f} | {entry['allocated_time']:<8.1f}")

# Available study time (replace with your desired value)
available_time = 6

# Calculate and print timetable
timetable = calculate_timetable(subjects, priorities, marks, available_time)
print("\nTimetable:")
print_timetable(timetable)
