
class AVLNode:
    def __init__(self, patient_id, patient_name):
        self.key = patient_id
        self.name = patient_name
        self.left = None
        self.right = None
        self.height = 1


class AVL:

    def __init__(self):
        self.root = None
        self.comparisons = 0
        self.rotations = 0

    # Get node height
    def _height(self, node):
        if node is None:
            return 0
        return node.height

    # Update node height
    def _update_height(self, node):
        node.height = 1 + max(
            self._height(node.left),
            self._height(node.right)
        )

    # Calculate balance factor
    def _balance_factor(self, node):
        if node is None:
            return 0

        return (
            self._height(node.left)
            - self._height(node.right)
        )

    # Right rotation (LL case)
    def _right_rotate(self, y):
        x = y.left
        temp = x.right

        x.right = y
        y.left = temp

        self._update_height(y)
        self._update_height(x)

        self.rotations += 1

        return x

    # Left rotation (RR case)
    def _left_rotate(self, x):
        y = x.right
        temp = y.left

        y.left = x
        x.right = temp

        self._update_height(x)
        self._update_height(y)

        self.rotations += 1

        return y

    # Rebalance the tree
    def _rebalance(self, node):
        self._update_height(node)

        balance = self._balance_factor(node)

        # LL and LR cases
        if balance > 1:

            if self._balance_factor(node.left) < 0:
                node.left = self._left_rotate(node.left)

            return self._right_rotate(node)

        # RR and RL cases
        if balance < -1:

            if self._balance_factor(node.right) > 0:
                node.right = self._right_rotate(node.right)

            return self._left_rotate(node)

        return node

    # Insert a patient
    def insert(self, patient_id, patient_name):
        self.root = self._insert(
            self.root,
            patient_id,
            patient_name
        )

    def _insert(self, node, patient_id, patient_name):

        if node is None:
            return AVLNode(patient_id, patient_name)

        if patient_id < node.key:
            node.left = self._insert(
                node.left, patient_id, patient_name
            )

        elif patient_id > node.key:
            node.right = self._insert(
                node.right, patient_id, patient_name
            )

        else:
            node.name = patient_name
            return node

        return self._rebalance(node)

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
        self.root = self._delete(self.root, patient_id)

    def _delete(self, node, patient_id):

        if node is None:
            return None

        if patient_id < node.key:
            node.left = self._delete(
                node.left, patient_id
            )

        elif patient_id > node.key:
            node.right = self._delete(
                node.right, patient_id
            )

        else:
            # Node has no left child
            if node.left is None:
                return node.right

            # Node has no right child
            if node.right is None:
                return node.left

            # Node has two children
            successor = node.right

            while successor.left is not None:
                successor = successor.left

            node.key = successor.key
            node.name = successor.name

            node.right = self._delete(
                node.right, successor.key
            )

        return self._rebalance(node)

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

    # Calculate tree height
    def height(self):
        return self._height(self.root)

    # Check whether AVL tree is balanced
    def is_balanced(self):

        def check(node):
            if node is None:
                return True, 0

            left_ok, left_height = check(node.left)
            right_ok, right_height = check(node.right)

            balance = left_height - right_height

            actual_height = 1 + max(
                left_height,
                right_height
            )

            valid = (
                left_ok
                and right_ok
                and abs(balance) <= 1
                and node.height == actual_height
            )

            return valid, actual_height

        return check(self.root)[0]

    # Check BST property
    def is_bst(self):

        def check(node, low, high):
            if node is None:
                return True

            if low is not None and node.key <= low:
                return False

            if high is not None and node.key >= high:
                return False

            return (
                check(node.left, low, node.key)
                and check(node.right, node.key, high)
            )

        return check(self.root, None, None)
