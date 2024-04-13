from tabulate import tabulate

# Initialize a 2D list to represent the timetable (48 slots for each day)
timetable = [[{'busy': False, 'rest': False} for _ in range(48)] for _ in range(7)]

# Function to mark busy slots for a specific day
def mark_busy_slots(day, busy_slots):
    for slot in busy_slots:
        timetable[day][slot]['busy'] = True

# Example: Marking busy slots for each day
busy_slots_per_day = [
    [0, 5, 6, 7, 20, 21, 22, 23, 24, 25, 35, 36, 37],  # Monday
    [8, 9, 10, 11, 12, 25, 26, 27, 28, 38, 39, 40],  # Tuesday
    [15, 16, 17, 18, 19, 30, 31, 32, 33, 43, 44, 45],  # Wednesday
    [0, 1, 2, 3, 4, 15, 16, 17, 18, 28, 29, 30],  # Thursday
    [10, 11, 12, 13, 14, 25, 26, 27, 28, 38, 39, 40],  # Friday
    [20, 21, 22, 23, 24, 35, 36, 37, 47],  # Saturday
    [0, 1, 3, 15, 16, 17, 18, 28, 29, 30],  # Sunday
]

for day, busy_slots in enumerate(busy_slots_per_day):
    mark_busy_slots(day, busy_slots)

days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Function to calculate the total number of free slots each day
def count_free_slots(day):
    return sum(1 for slot in timetable[day] if not slot['busy'] and not slot['rest'])

def distribute_study_hours_with_dynamic_rest(subjects, total_hours, rest_duration=0.5):
    study_plan = {}
    for subject, hours in zip(subjects, total_hours):
        study_plan[subject] = {day: [] for day in days_of_week}
        total_hours_needed = hours
        hours_per_day = total_hours_needed / 7
        remainder = total_hours_needed % 7

        for day in range(7):
            free_slots = [index for index, slot in enumerate(timetable[day]) if not slot['busy'] and not slot['rest']]
            busy_slots = [index for index, slot in enumerate(timetable[day]) if slot['busy']]

            # Calculate the number of hours to assign to this day
            if day < remainder:
                hours_to_assign = int(hours_per_day) + 1
            else:
                hours_to_assign = int(hours_per_day)

            # Assign the hours to the free slots with dynamic rest
            i = 0
            rest_hours_to_assign = 0  # Initialize rest duration
            while i < hours_to_assign and free_slots:
                # Assign study slot
                slot = free_slots.pop(0)
                study_plan[subject][days_of_week[day]].append(slot)
                timetable[day][slot]['busy'] = True  # Mark the slot as busy

                i += 1  # Increment the study hour count

                if i >= 2:  # If studied for 2 or more hours
                    rest_hours_to_assign = min(i * rest_duration, 1)  # Max rest duration is 1 hour
                    for _ in range(int(rest_hours_to_assign / rest_duration)):
                        if free_slots:
                            # Assign rest slot
                            rest_slot = free_slots.pop(0)
                            timetable[day][rest_slot]['rest'] = True  # Mark the rest slot as rest

                i += rest_hours_to_assign
            
    return study_plan

chains = ['LinkedList', 'Stack', 'Tree', 'Searching', 'Sorting'] #EXAMPLE
total_hours = [9, 14, 13, 13, 13]

study_plan_with_dynamic_rest = distribute_study_hours_with_dynamic_rest(chains, total_hours)

def print_timetable_with_study_plan(timetable, study_plan, days_of_week):
    for day in days_of_week:
        for slot in range(48):
            if any(slot in study_plan[subject][day] for subject in study_plan if day in study_plan[subject]):
                for subject in study_plan:
                    if day in study_plan[subject] and slot in study_plan[subject][day]:
                        print(f"{subject} ", end="")
                        break
            elif timetable[days_of_week.index(day)][slot]['rest']:
                print(f"Rest ", end="")
            elif timetable[days_of_week.index(day)][slot]['busy']:
                print(f"Busy ", end="")
            else:
                print(f"Empty ", end="")

print_timetable_with_study_plan(timetable, study_plan_with_dynamic_rest, days_of_week)