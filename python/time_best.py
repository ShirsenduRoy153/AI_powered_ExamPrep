from datetime import datetime, timedelta

data = {
    'timestamp': ['2022-01-01 1:00:00', '2022-01-02 10:30:00', '2022-01-03 15:45:00', '2022-01-04 14:00:00',
                  '2022-01-06 1:30:00', '2022-01-06 1:15:00', '2022-01-07 09:45:00', '2022-01-08 20:00:00',
                  '2022-01-09 1:30:00', '2022-01-10 1:20:00'],  
    'stress_level': [3, 1, 2, 5, 1, 3, 4, 2, 5, 1],  
    'concentration_level': [8, 10, 9, 6, 10, 8, 7, 9, 6, 10],  
    'study_time': [60, 90, 90, 50, 20, 55, 70, 100, 40, 110],  # in minutes
    'marks': [80, 95, 95, 85, 5, 8, 75, 90, 85, 5],  # exam marks
}

current_datetime = datetime.now()

future_timestamps = [timestamp for timestamp in data['timestamp'] if datetime.strptime(timestamp, '%Y-%m-%d %H:%M:%S') > current_datetime]

if future_timestamps:
    best_index = max(
        range(len(future_timestamps)),
        key=lambda i: (0.4 * (data['marks'][i]/100) + 0.3 * data['concentration_level'][i] + 0.3 * (1 - data['stress_level'][i]/5))
    )

    # Generate a list of potential study times by excluding existing timestamps
    potential_study_times = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in data['timestamp']]
    potential_study_times = [time for time in potential_study_times if time != datetime.strptime('01:30:00', '%H:%M:%S')]

    # Choose the mode from potential study times as the preferred study time
    preferred_study_time = max(set(potential_study_times), key=potential_study_times.count)

    # Perform additional calculation on the preferred study time (e.g., rounding based on stress and concentration levels)
    rounded_study_time = preferred_study_time + timedelta(minutes=(data['stress_level'][best_index] * 5) + (data['concentration_level'][best_index] * 3))

    print("Best Time to Study:")
    print("Preferred Study Time (Original):", preferred_study_time.strftime('%H:%M:%S'))
    print("Rounded Study Time:", rounded_study_time.strftime('%H:%M:%S'))
    print("Concentration Level:", data['concentration_level'][best_index])
    print("Stress Level:", data['stress_level'][best_index])
    print("Exam Marks:", data['marks'][best_index])

    # Add personalized comments based on performance
    if data['marks'][best_index] >= 80:
        print("Congratulations! You've been consistently performing well. Keep up the good work!")
    elif data['marks'][best_index] >= 60:
        print("You're doing well, but there's always room for improvement. Consider focusing more on specific topics.")
    else:
        print("You might want to revise and put in some extra effort for better results.")

else:
    best_index = max(
        range(len(data['timestamp'])),
        key=lambda i: (0.4 * (data['marks'][i]/100) + 0.3 * data['concentration_level'][i] + 0.3 * (1 - data['stress_level'][i]/5))
    )
    best_timestamp = data['timestamp'][best_index]

    # Generate a list of potential study times by excluding existing timestamps
    potential_study_times = [datetime.strptime(ts, '%Y-%m-%d %H:%M:%S') for ts in data['timestamp']]
    potential_study_times = [time for time in potential_study_times if time != datetime.strptime('01:30:00', '%H:%M:%S')]

    # Choose the mode from potential study times as the preferred study time
    preferred_study_time = max(set(potential_study_times), key=potential_study_times.count)

    # Perform additional calculation on the preferred study time (e.g., rounding based on stress and concentration levels)
    rounded_study_time = preferred_study_time + timedelta(minutes=(data['stress_level'][best_index] * 5) + (data['concentration_level'][best_index] * 3))

    print("Best Time to Study (Highest Concentration and Marks):")
    print("Preferred Study Time (Original):", preferred_study_time.strftime('%H:%M:%S'))
    print("Rounded Study Time:", rounded_study_time.strftime('%H:%M:%S'))
    print("Concentration Level:", data['concentration_level'][best_index])
    print("Stress Level:", data['stress_level'][best_index])
    print("Exam Marks:", data['marks'][best_index])

    # Add personalized comments based on performance
    if data['marks'][best_index] >= 80:
        print("Congratulations! You've been consistently performing well. Keep up the good work!")
    elif data['marks'][best_index] >= 60:
        print("You're doing well, but there's always room for improvement. Consider focusing more on specific topics.")
    else:
        print("You might want to revise and put in some extra effort for better results.")
