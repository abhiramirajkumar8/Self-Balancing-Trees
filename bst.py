
class BSTNode:
    def __init__(self, patient_id, patient_name):
        self.key = patient_id
        self.name = patient_name
        self.left = None
        self.right = None


class BST:

    def __init__(self):
        self.root = None
        self.comparisons = 0

    # Insert a patient
    def insert(self, patient_id, patient_name):
        new_node = BSTNode(patient_id, patient_name)

        if self.root is None:
            self.root = new_node
            return

        current = self.root

        while True:
            if patient_id == current.key:
                current.name = patient_name
                return

            elif patient_id < current.key:
                if current.left is None:
                    current.left = new_node
                    return
                current = current.left

            else:
                if current.right is None:
                    current.right = new_node
                    return
                current = current.right

    # Search for a patient
    def search(self, patient_id):
        self.comparisons = 0
        current = self.root

        while current is not None:
            self.comparisons += 1

            if patient_id == current.key:
                return current

            elif patient_id < current.key:
                current = current.left

            else:
                current = current.right

        return None

    # Delete a patient
    def delete(self, patient_id):
        parent = None
        current = self.root

        while current is not None and current.key != patient_id:
            parent = current

            if patient_id < current.key:
                current = current.left
            else:
                current = current.right

        if current is None:
            return False

        # Case 1 and 2: Zero or one child
        if current.left is None or current.right is None:

            if current.left is not None:
                child = current.left
            else:
                child = current.right

            if parent is None:
                self.root = child

            elif parent.left == current:
                parent.left = child

            else:
                parent.right = child

            return True

        # Case 3: Two children
        successor_parent = current
        successor = current.right

        while successor.left is not None:
            successor_parent = successor
            successor = successor.left

        current.key = successor.key
        current.name = successor.name

        if successor_parent.left == successor:
            successor_parent.left = successor.right
        else:
            successor_parent.right = successor.right

        return True

    # In-order traversal
    def inorder(self):
        result = []
        stack = []
        current = self.root

        while stack or current is not None:

            while current is not None:
                stack.append(current)
                current = current.left

            current = stack.pop()

            result.append((current.key, current.name))

            current = current.right

        return result

    # Calculate height
    def height(self):
        if self.root is None:
            return 0

        max_height = 0
        stack = [(self.root, 1)]

        while stack:
            node, depth = stack.pop()

            max_height = max(max_height, depth)

            if node.left is not None:
                stack.append((node.left, depth + 1))

            if node.right is not None:
                stack.append((node.right, depth + 1))

        return max_height

    # Check BST property
    def is_bst(self):
        if self.root is None:
            return True

        stack = [(self.root, None, None)]

        while stack:
            node, low, high = stack.pop()

            if low is not None and node.key <= low:
                return False

            if high is not None and node.key >= high:
                return False

            if node.left is not None:
                stack.append((node.left, low, node.key))

            if node.right is not None:
                stack.append((node.right, node.key, high))

        return True
