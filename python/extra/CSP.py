import random

# Data structures for representing subjects and assignments
class Subject:
    def __init__(self, name, priority):
        self.name = name
        self.priority = priority

class Assignment:
    def __init__(self, subject, day, slot):
        self.subject = subject
        self.day = day
        self.slot = slot

# Function to check if an assignment is valid (replace with actual logic)
def is_valid_assignment(assignments, new_assignment):
    # Replace with actual constraint checking logic
    return True

def generate_timetable_csp(subjects):
    assignments = []

    def backtrack(index):
        if index == len(subjects):
            return True  # All subjects have been assigned

        subject = subjects[index][0]  # Extract subject name from tuple

        # Find the corresponding Subject instance
        subject_instance = next((s for s in subject_objects if s.name == subject), None)

        if subject_instance is None:
            return False  # Subject instance not found

        # Iterate through possible days and slots for the subject
        for day in range(5):
            for slot in range(6):
                new_assignment = Assignment(subject_instance, day, slot)

                # Check if the assignment is valid
                if is_valid_assignment(assignments, new_assignment):
                    assignments.append(new_assignment)

                    if backtrack(index + 1):
                        return True

                    assignments.pop()  # Backtrack if assignment didn't lead to a solution

        return False  # No valid assignments found for this subject

    # Convert input_data to Subject instances
    subject_objects = [Subject(name, priority) for name, priority in subjects]

    if backtrack(0):
        return assignments
    else:
        return None

days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']  # Weekdays

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

input_data.sort(key=lambda x: x[1], reverse=True)

# Generate timetable using CSP algorithm
timetable = generate_timetable_csp(input_data)

if timetable:
    # Print the generated timetable
    print("Final Timetable:")

    # Separate counter for weekday index
    weekday_index = 0

    for i, slot_info in enumerate(timetable, start=1):
        # Print slot information: weekday name, slot number, subject name
        print(f"{days[weekday_index]}: Slot {i}: {slot_info.subject.name}")

        # Reset the weekday index after each iteration
        weekday_index = (weekday_index + 1) % len(days)

else:
    print("No valid timetable found")