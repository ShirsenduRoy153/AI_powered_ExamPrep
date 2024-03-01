def generate_timetable(subjects, rest_duration, sleep_after=True):

    from datetime import datetime, timedelta

    # Sorting in descending order
    subjects.sort(key=lambda subject: subject["priority"], reverse=True)

    # VARIABLES
    timetable = []
    current_time = datetime.today()

    # Iterate through subjects
    for subject in subjects:
        # Schedule the subject
        start_time = current_time
        end_time = start_time + timedelta(hours=subject["required_time"])
        timetable.append({"subject": subject["name"], "start_time": start_time, "end_time": end_time})

        # Add a fixed 30-minute rest after each subject (except "Dynamic Programming")
        if subject["name"] != "Dynamic Programming":
            rest_time = end_time + timedelta(hours=rest_duration)
            timetable.append({"subject": "Rest", "start_time": end_time, "end_time": rest_time, "rest_time": rest_duration})
            current_time = rest_time

    # Calculate remaining time for sleep (only if sleep_after is True)
    if sleep_after:
        sleep_duration = timedelta(hours=24) - (current_time - datetime.today())
        timetable.append({"subject": "Sleep", "start_time": current_time, "end_time": current_time + sleep_duration, "sleep_time": sleep_duration.total_seconds() / 3600})

    return timetable

# Example usage and printing the timetable remain the same

# Example usage
subjects = [
    {"name": "Linked List", "priority": 1.17, "required_time": 1.0, },
    {"name": "Stack", "priority": 1.33, "required_time": 1.0, },
    {"name": "Queue", "priority": 0.90, "required_time": 0.5, },
    {"name": "Tree", "priority": 1.20, "required_time": 1.0, },
    {"name": "Graph", "priority": 2.63, "required_time": 3.5, },
    {"name": "Hashing", "priority": 1.60, "required_time": 2.5, },
    {"name": "Heap", "priority": 1.35, "required_time": 1.0, },
    {"name": "Sorting", "priority": 1.20, "required_time": 1.0, },
    {"name": "Searching", "priority": 1.17, "required_time": 1.0, },
    {"name": "Dynamic Programming", "priority": 0.90, "required_time": 1.0, },
]

rest_duration = 0.5  # 30 minutes

# Generate timetable with 30-minute rest and sleep
timetable = generate_timetable(subjects, rest_duration)

# Print the timetable
for entry in timetable:
    start_time = entry["start_time"].strftime("%H:%M")
    end_time = entry["end_time"].strftime("%H:%M")
    if "rest_time" in entry:
        rest_time = f"{entry['rest_time']:.2f} hours"
    elif "sleep_time" in entry:
        rest_time = f"{entry['sleep_time']:.2f} hours"
    else:
        rest_time = ""
    print(f"{entry['subject']}: {start_time} - {end_time}")