import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Function to categorize time into slots
def categorize_time(timestamp):
    hour = timestamp.hour
    if 5 <= hour < 9:
        return 'Morning'
    elif 9 <= hour < 12:
        return 'Late Morning'
    elif 12 <= hour < 15:
        return 'Early Afternoon'
    elif 15 <= hour < 18:
        return 'Late Afternoon'
    elif 18 <= hour < 21:
        return 'Early Evening'
    elif 21 <= hour < 24:
        return 'Late Evening'
    elif 0 <= hour < 3:
        return 'Night'
    else:
        return 'Late Night'

# Sample data with at least 8 data points
data = {
    'Timestamp': ['2024-01-31 08:00', '2024-01-31 10:00', '2024-01-31 13:30',
                   '2024-01-31 16:00', '2024-01-31 19:00', '2024-01-31 22:00',
                   '2024-02-01 02:00', '2024-02-01 04:00'],
    'StressLevel': [2, 1, 3, 4, 2, 3, 2, 1],
    'ConcentrationLevel': [8, 9, 7, 6, 8, 5, 9, 7],
    'TestMarks': [80, 90, 75, 60, 85, 70, 95, 88],
    'StudyTime': [60, 90, 120, 75, 80, 100, 110, 70]  # in minutes
}

# Create a DataFrame from the data
df = pd.DataFrame(data)
df['Timestamp'] = pd.to_datetime(df['Timestamp'])

# Categorize time into slots
df['TimeSlot'] = df['Timestamp'].apply(categorize_time)

# Calculate more complex study score for each session
df['StudyScore'] = (df['ConcentrationLevel'] ** 0.5 * 
                    (df['TestMarks'] + 1).apply(lambda x: np.log(x)) -
                    (df['StressLevel'] ** (1/3) * df['StudyTime'] ** 0.5))

# Calculate average study score for each time slot
study_score_by_slots = df.groupby('TimeSlot')['StudyScore'].mean()

# Find the best time slot with the highest average study score
best_time_slot = study_score_by_slots.idxmax()

# Plot average study score over time slots using a bar graph
plt.figure(figsize=(10, 6))
study_score_by_slots.plot(kind='bar', color='purple')
plt.xlabel('Time Slot')
plt.ylabel('Average Study Score')
plt.title('Average Study Score Over Time Slots')
plt.xticks(rotation=90)
plt.show()

# Display the DataFrame with study scores and study time
print("DataFrame with Study Scores and Study Time:")
print(df[['Timestamp', 'StressLevel', 'ConcentrationLevel', 'TestMarks', 'StudyTime', 'StudyScore']])
print("\nBest Time to Study:", best_time_slot)
