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
    'Engineering Mathematics': {'score': 5, 'stress_level': 3},
    'Digital Logic': {'score': 4, 'stress_level': 2},
    'Computer Organization and Architecture': {'score': 6, 'stress_level': 1},
    'Programming and Data Structures': {'score': 3, 'stress_level': 4},
    'Algorithms': {'score': 5, 'stress_level': 3},
    'Theory of Computation': {'score': 4, 'stress_level': 2},
    'Compiler Design': {'score': 6, 'stress_level': 1},
    'Operating System': {'score': 3, 'stress_level': 4},
    'Databases': {'score': 5, 'stress_level': 3},
    'Computer Networks': {'score': 4, 'stress_level': 2},
    'Software Engineering': {'score': 6, 'stress_level': 1}
}

data = []

for subject, details in subject_details.items():
    priority = details['priority']
    difficulty = details['difficulty']
    peak_concentration = user_data[subject]['score']
    stress_level = user_data[subject]['stress_level']
    
    adjusted_priority = priority - (difficulty == 'hard') * 0.5
    adjusted_priority -= (adjusted_priority * (stress_level / 10))
    adjusted_priority *= (peak_concentration / 6) 
    
    data.append([subject, round(adjusted_priority, 2)])

table = pd.DataFrame(data, columns=['Subject', 'Adjusted Priority'])

print(table)
