import pandas as pd

subject_details = {
    'Engineering Mathematics': {'priority': 2, 'difficulty': 'medium'},
    'Digital Logic': {'priority': 3, 'difficulty': 'hard'},
    'Computer Organization and Architecture': {'priority': 1, 'difficulty': 'easy'},
    'Programming and Data Structures': {'priority': 4, 'difficulty': 'medium'},
    'Algorithms': {'priority': 5, 'difficulty': 'hard'},
    'Theory of Computation': {'priority': 3, 'difficulty': 'medium'},
    'Compiler Design': {'priority': 2, 'difficulty': 'hard'},
    'Operating System': {'priority': 4, 'difficulty': 'medium'},
    'Databases': {'priority': 2, 'difficulty': 'medium'},
    'Computer Networks': {'priority': 3, 'difficulty': 'medium'},
    'Software Engineering': {'priority': 1, 'difficulty': 'easy'}
}

user_data = {
    'Engineering Mathematics': {'peak_concentration_hours': 5, 'stress_level': 3},
    'Digital Logic': {'peak_concentration_hours': 4, 'stress_level': 2},
    'Computer Organization and Architecture': {'peak_concentration_hours': 6, 'stress_level': 1},
    'Programming and Data Structures': {'peak_concentration_hours': 3, 'stress_level': 4},
    'Algorithms': {'peak_concentration_hours': 5, 'stress_level': 3},
    'Theory of Computation': {'peak_concentration_hours': 4, 'stress_level': 2},
    'Compiler Design': {'peak_concentration_hours': 6, 'stress_level': 1},
    'Operating System': {'peak_concentration_hours': 3, 'stress_level': 4},
    'Databases': {'peak_concentration_hours': 5, 'stress_level': 3},
    'Computer Networks': {'peak_concentration_hours': 4, 'stress_level': 2},
    'Software Engineering': {'peak_concentration_hours': 6, 'stress_level': 1}
}

data = []

for subject, details in subject_details.items():
    priority = details['priority']
    difficulty = details['difficulty']
    peak_concentration = user_data[subject]['peak_concentration_hours']
    stress_level = user_data[subject]['stress_level']
    
    adjusted_priority = priority - (difficulty == 'hard') * 0.5
    adjusted_priority -= (adjusted_priority * (stress_level / 10))
    adjusted_priority *= (peak_concentration / 6) 
    
    data.append([subject, priority, difficulty, peak_concentration, stress_level, round(adjusted_priority, 2)])

table = pd.DataFrame(data, columns=['Subject', 'Priority Score', 'Difficulty Level', 'Peak Concentration Hours', 'Stress Level', 'Adjusted Priority'])

print(table)
