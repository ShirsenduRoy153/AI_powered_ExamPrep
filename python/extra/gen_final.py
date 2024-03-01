import random
import statistics

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
    'LinkedList': 100,
    'Stack': 90,
    'Queue': 100,
    'Tree': 54,
    'Graph': 34,
    'Hashing': 23,
    'Heap': 25,
    'Sorting': 18,
    'Searching': 23,
    'DynamicProgramming': 11,
}


def calculate_dependency_score(subject):
    """
    Calculates a score based on the number of dependencies a subject has.
    - Subjects with fewer dependencies get higher scores.
    """
    return len(DEPENDENCIES.get(subject, [])) * -1


def generate_timetable():
    subjects = list(DEPENDENCIES.keys())

    # Sort subjects by a combination of dependency score and performance
    subjects.sort(key=lambda x: (calculate_dependency_score(x), PERFORMANCE[x]))

    return subjects


def rate_timetable(timetable):
    total_performance = sum(PERFORMANCE[subject] for subject in timetable)
    return total_performance / len(timetable)


def balance(timetable):
    performance_scores = [PERFORMANCE[subject] for subject in timetable]
    return statistics.variance(performance_scores)


def dependencies_met(subject, timetable):
    # Check if all dependencies of a subject are in the timetable
    return all(dep in timetable for dep in DEPENDENCIES.get(subject, []))


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

        if user_rating <= 4:
            # If poorly rated, remove a subject randomly
            subject_to_remove = random.choice(best_timetable)
            best_timetable.remove(subject_to_remove)

        if user_rating >= 5:
            break  # Stop if the user is satisfied

        # Filter based on balance and prioritize low dependency subjects
        population.sort(key=lambda x: (balance(x), calculate_dependency_score(x[0])))
        population = population[:population_size // 2]

    return best_timetable


final_timetable = genetic_algorithm()

print("Final Timetable:", final_timetable)