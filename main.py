
from bst import BST
from avl import AVL


# Display tree details
def display_results(tree, name):

    print("\n", name)

    print(
        "Root:",
        tree.root.key if tree.root else None
    )

    print("Height:", tree.height())

    print(
        "In-order traversal:",
        [key for key, name in tree.inorder()]
    )


# Test BST deletion cases
def test_bst_deletion():

    # Leaf node deletion
    tree = BST()

    for key in [20, 10, 30]:
        tree.insert(key, "Patient")

    assert tree.delete(10)
    assert tree.is_bst()

    # One child deletion
    tree = BST()

    for key in [20, 10, 5]:
        tree.insert(key, "Patient")

    assert tree.delete(10)
    assert tree.is_bst()

    # Two children deletion
    tree = BST()

    for key in [20, 10, 30, 25, 40]:
        tree.insert(key, "Patient")

    assert tree.delete(20)
    assert tree.is_bst()

    print("All BST deletion tests passed!")


# Test all four AVL rotations
def test_avl_rotations():

    cases = [
        [30, 20, 10],  # LL
        [10, 20, 30],  # RR
        [30, 10, 20],  # LR
        [10, 30, 20]   # RL
    ]

    for sequence in cases:

        tree = AVL()

        for key in sequence:
            tree.insert(key, "Patient")

        assert tree.is_balanced()
        assert tree.is_bst()
        assert tree.root.key == 20

    print("All four AVL rotation tests passed!")


# Main demonstration
def main():

    patient_data = [
        (10, "Arun"),
        (20, "Rahul"),
        (30, "Priya"),
        (40, "Anu"),
        (50, "Kiran"),
        (25, "Meera")
    ]

    bst = BST()
    avl = AVL()

    # Insert patient records
    for patient_id, name in patient_data:

        bst.insert(patient_id, name)
        avl.insert(patient_id, name)

    # Display results
    display_results(bst, "NORMAL BST")
    display_results(avl, "AVL TREE")

    print("\nAVL Rotations:", avl.rotations)

    print("BST Property:", bst.is_bst())
    print("AVL BST Property:", avl.is_bst())
    print("AVL Balanced:", avl.is_balanced())

    # Search example
    result = avl.search(25)

    print(
        "\nSearch Patient ID 25:",
        result.name if result else "Not found"
    )

    print("Search Comparisons:", avl.comparisons)

    # Delete example
    avl.delete(20)

    print("\nAfter deleting Patient ID 20:")

    print(
        "In-order:",
        [key for key, name in avl.inorder()]
    )

    print("Height:", avl.height())
    print("Balanced:", avl.is_balanced())

    # Run tests
    test_bst_deletion()
    test_avl_rotations()


if __name__ == "__main__":
    main()
