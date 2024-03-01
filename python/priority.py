import pandas as pd

subject_details = {
    'Linked List': {'priority': 2, 'difficulty': 'medium'},
    'Stack': {'priority': 3, 'difficulty': 'hard'},
    'Queue': {'priority': 1, 'difficulty': 'easy'},
    'Tree': {'priority': 4, 'difficulty': 'medium'},
    'Graph': {'priority': 5, 'difficulty': 'hard'},
    'Hashing': {'priority': 3, 'difficulty': 'medium'},
    'Heap': {'priority': 2, 'difficulty': 'hard'},
    'Sorting': {'priority': 4, 'difficulty': 'medium'},
    'Searching': {'priority': 2, 'difficulty': 'medium'},
    'Dynamic Programming': {'priority': 1, 'difficulty': 'easy'}
}

user_data = {
    'Linked List': {'score': 1, 'rating': 1},
    'Stack': {'score': 4, 'rating': 2},
    'Queue': {'score': 5, 'rating': 1},
    'Tree': {'score': 3, 'rating': 4},
    'Graph': {'score': 5, 'rating': 3},
    'Hashing': {'score': 4, 'rating': 2},
    'Heap': {'score': 5, 'rating': 1},
    'Sorting': {'score': 3, 'rating': 4},
    'Searching': {'score': 0, 'rating': 3},
    'Dynamic Programming': {'score': 3, 'rating': 4}
}

data = []

for subject, details in subject_details.items():
    priority = details['priority']
    difficulty = details['difficulty']
    peak_concentration = user_data[subject]['score']
    rating = user_data[subject]['rating']
    
    # Adjust priority based on difficulty
    if difficulty == 'hard':
        priority += 0.5
    elif difficulty == 'medium':
        priority += 0.35
    elif difficulty == 'easy':
        priority += 0.2
    
    # Adjust priority based on score and rating (lower rating and lower marks result in higher priority)
    adjusted_priority = priority * (1 - peak_concentration / 6) * (1 - rating / 10)
    
    data.append([subject, round(adjusted_priority, 2)])

table = pd.DataFrame(data, columns=['Subject', 'Adjusted Priority'])

print(table)
