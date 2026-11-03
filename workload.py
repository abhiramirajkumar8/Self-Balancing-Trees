
import random


def generate_datasets(n, seed=42):

    # Dataset 1: Sequential
    sequential = list(range(1, n + 1))

    # Dataset 2: Random
    random_ids = sequential.copy()

    rng = random.Random(seed + n)
    rng.shuffle(random_ids)

    # Dataset 3: Nearly sorted
    nearly_sorted = sequential.copy()

    number_of_swaps = max(1, int(n * 0.05))

    for i in range(number_of_swaps):

        first = rng.randrange(n)
        second = rng.randrange(n)

        nearly_sorted[first], nearly_sorted[second] = (
            nearly_sorted[second],
            nearly_sorted[first]
        )

    return {
        "Sequential": sequential,
        "Random": random_ids,
        "Nearly sorted": nearly_sorted
    }
