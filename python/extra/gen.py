import random

DEPENDENCIES = {
    'LinkedList': ['Stack', 'Queue'],
    'Stack': ['Tree', 'Graph'],
    'Queue': ['Hashing', 'Heap'],
    'Tree': ['Sorting', 'Searching'],
    'Graph': ['Heap', 'DynamicProgramming'],
    'Hashing': [],
    'Heap': [],
    'Sorting': [],
    'Searching': [],
    'DynamicProgramming': [],
}

PERFORMANCE = {
    'LinkedList': 60,
    'Stack': 48,
    'Queue': 48,
    'Tree': 54,
    'Graph': 34,
    'Hashing': 23,
    'Heap': 25,
    'Sorting': 18,
    'Searching': 23,
    'DynamicProgramming': 11,
}

# Function to generate a random timetable
def generate_timetable():
    timetable = list(DEPENDENCIES.keys())
    random.shuffle(timetable)
    return timetable

# Function to evaluate the performance of a timetable
def rate_timetable(timetable):
    total_performance = sum(PERFORMANCE[subject] for subject in timetable)
    return total_performance / len(timetable)

# Genetic Algorithm to evolve timetables based on performance ratings
def genetic_algorithm(generations=5, population_size=10):
    best_timetable = None
    best_rating = 0

    for _ in range(generations):
        population = [generate_timetable() for _ in range(population_size)]

        for timetable in population:
            rating = rate_timetable(timetable)
            if rating > best_rating:
                best_rating = rating
                best_timetable = timetable

        print("Generation:", _, "Best Timetable:", best_timetable)
        print("Best Rating:", best_rating)

        user_rating = float(input("Rate the timetable (out of 5): "))
        if user_rating >= 3:
            break  # Stop if the user is satisfied

    return best_timetable

# Run the genetic algorithm
final_timetable = genetic_algorithm()

print("Final Timetable:", final_timetable)
