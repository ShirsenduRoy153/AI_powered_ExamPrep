import pandas as pd

# Create a DataFrame
data = {
    'Subject': ['Linked List',
                 'Stack', 
                 'Queue', 
                 'Tree', 
                 'Graph', 
                 'Hashing', 
                 'Heap', 
                 'Sorting', 
                 'Searching', 
                 'Dynamic Programming'],
    "Adjusted Priority": [1.17, 1.33, 0.90, 1.20, 4.63, 3.60, 1.35, 1.20, 1.17, 1.00]
}

df = pd.DataFrame(data)

# Calculate total slots and slots per subject based on priority
total_slots = 20
slots_per_subject = df["Adjusted Priority"] * total_slots / df["Adjusted Priority"].sum()

# Round slots to nearest integer
slots_per_subject = slots_per_subject.apply(lambda x: round(x))

# Assume each slot is 30 minutes
slot_duration = 30  # minutes

# Calculate total time for each subject in hours and minutes
total_hours_per_subject = slots_per_subject // 2
total_minutes_per_subject = (slots_per_subject % 2) * 30

# Create a new DataFrame with subject, slots, and time
slots_df = pd.DataFrame({
    "Subject": df["Subject"],
    "Minimum Slots required ": slots_per_subject,
    "Required Time (hours:minutes)": [f"{h} hr {m} mins" for h, m in zip(total_hours_per_subject, total_minutes_per_subject)]
})

# Print the DataFrame
print(slots_df.to_string())
