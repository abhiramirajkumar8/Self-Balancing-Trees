
import csv
import math
import random
import time

from bst import BST
from avl import AVL
from workload import generate_datasets


SIZES = [1000, 5000, 10000]
SEARCH_TRIALS = 1000
SEED = 42


# Measure insertion time
def build_tree(tree, ids):

    start = time.perf_counter()

    for patient_id in ids:
        tree.insert(
            patient_id,
            "Patient_" + str(patient_id)
        )

    end = time.perf_counter()

    return end - start


# Calculate average search comparisons
def average_search_comparisons(tree, ids, seed):

    rng = random.Random(seed)

    selected_ids = rng.choices(
        ids,
        k=SEARCH_TRIALS
    )

    total = 0

    for patient_id in selected_ids:

        result = tree.search(patient_id)

        if result is None:
            raise AssertionError("Patient not found")

        total += tree.comparisons

    return total / SEARCH_TRIALS


# Generate comparison graph
def create_graph(results):

    import matplotlib.pyplot as plt

    sequential = [
        row for row in results
        if row["Dataset"] == "Sequential"
    ]

    bst_rows = sorted(
        [r for r in sequential if r["Tree"] == "BST"],
        key=lambda r: r["N"]
    )

    avl_rows = sorted(
        [r for r in sequential if r["Tree"] == "AVL"],
        key=lambda r: r["N"]
    )

    sizes = [r["N"] for r in bst_rows]

    bst_heights = [
        r["Final height"] for r in bst_rows
    ]

    avl_heights = [
        r["Final height"] for r in avl_rows
    ]

    plt.figure(figsize=(8, 5))

    plt.plot(
        sizes,
        bst_heights,
        marker="o",
        label="Normal BST"
    )

    plt.plot(
        sizes,
        avl_heights,
        marker="o",
        label="AVL Tree"
    )

    plt.xlabel("Number of Patient IDs")
    plt.ylabel("Tree Height")

    plt.title("BST vs AVL Tree Height")

    plt.xticks(sizes)
    plt.legend()
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("comparison.png", dpi=300)

    plt.close()


# Run all experiments
def run_experiments():

    results = []

    for n in SIZES:

        datasets = generate_datasets(n, SEED)

        for dataset_name, ids in datasets.items():

            # Same deletion IDs for both trees
            rng = random.Random(SEED + n + 999)

            deletion_ids = rng.sample(
                range(1, n + 1),
                int(n * 0.20)
            )

            for tree_name, TreeClass in [
                ("BST", BST),
                ("AVL", AVL)
            ]:

                tree = TreeClass()

                # Insertion
                insertion_time = build_tree(tree, ids)

                assert tree.is_bst()

                if tree_name == "AVL":
                    assert tree.is_balanced()

                final_height = tree.height()

                # Search
                average_comparisons = (
                    average_search_comparisons(
                        tree,
                        ids,
                        SEED + n
                    )
                )

                rotations = (
                    tree.rotations
                    if tree_name == "AVL"
                    else 0
                )

                # Deletion of 20% keys
                for patient_id in deletion_ids:
                    tree.delete(patient_id)

                assert tree.is_bst()

                if tree_name == "AVL":
                    assert tree.is_balanced()

                # Save results
                row = {
                    "Dataset": dataset_name,
                    "N": n,
                    "Tree": tree_name,
                    "Final height": final_height,
                    "Minimum height": math.ceil(
                        math.log2(n + 1)
                    ),
                    "Insertion time": round(
                        insertion_time, 6
                    ),
                    "Average search comparisons": round(
                        average_comparisons, 3
                    ),
                    "Total rotations": rotations,
                    "Height after deletion": tree.height()
                }

                results.append(row)

                print(
                    dataset_name,
                    n,
                    tree_name,
                    "Height:", final_height,
                    "Comparisons:", round(
                        average_comparisons, 3
                    ),
                    "Rotations:", rotations,
                    "Height after deletion:", tree.height()
                )

    # Export CSV
    with open(
        "results.csv",
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.DictWriter(
            file,
            fieldnames=results[0].keys()
        )

        writer.writeheader()
        writer.writerows(results)

    # Create graph
    try:
        create_graph(results)
        print("\nGraph saved as comparison.png")

    except ImportError:
        print("\nInstall matplotlib using pip install matplotlib")

    print("\nResults saved in results.csv")
    print("All experiments completed!")


if __name__ == "__main__":
    run_experiments()
