
# Lab Question 6 – Self-Balancing Binary Search Tree

## Project Description

This project implements and compares a normal Binary Search Tree (BST) and an AVL Tree using Python.

The project is based on the MediQueue telemedicine scenario, where patient records are stored using unique Patient IDs.

Both trees support insertion, searching, deletion and in-order traversal.

## Requirements

- Python 3
- Matplotlib library

Install Matplotlib:

    pip install matplotlib

## Project Files

1. bst.py – Implements the normal Binary Search Tree.
2. avl.py – Implements the AVL Tree with four rotations.
3. workload.py – Generates three types of datasets.
4. experiment.py – Performs experiments and compares both trees.
5. main.py – Demonstrates tree operations and tests.
6. README.md – Project documentation.

## How to Run

Step 1: Open the project folder in VS Code.

Step 2: Open the terminal.

Step 3: Install Matplotlib:

    pip install matplotlib

Step 4: Run the sample demonstration:

    python main.py

Step 5: Run the experiments:

    python experiment.py

## Workload Generation

Three datasets are generated:

1. Sequential Dataset – Patient IDs in ascending order.
2. Random Dataset – Patient IDs in random order.
3. Nearly Sorted Dataset – Sorted IDs with approximately 5% random swaps.

Each dataset is tested with:

- N = 1000
- N = 5000
- N = 10000

A fixed random seed is used to make results reproducible.

## Performance Measurements

The program measures:

- Final tree height.
- Theoretical minimum height.
- Total insertion time.
- Average search comparisons.
- AVL rotations.
- Height after deleting 20% of the keys.

## Output Files

After running experiment.py:

- results.csv – Contains experimental comparison results.
- comparison.png – Displays the graph comparing BST and AVL heights.

## Conclusion

The experiment compares the performance of a normal BST and an AVL Tree.

A normal BST may become unbalanced when IDs are inserted in sorted order. An AVL Tree automatically balances itself using rotations.

The final conclusion should be written using the actual experimental results obtained from the program.
