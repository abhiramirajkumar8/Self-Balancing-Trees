
class Node:
    def __init__(self, data, color="RED"):
        self.data = data
        self.color = color
        self.left = None
        self.right = None
        self.parent = None


class RedBlackTree:
    def __init__(self):
        self.NIL = Node(None, "BLACK")
        self.NIL.left = self.NIL
        self.NIL.right = self.NIL
        self.root = self.NIL
        self.rotations = 0

    def left_rotate(self, x):
        y = x.right
        x.right = y.left

        if y.left != self.NIL:
            y.left.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.left:
            x.parent.left = y
        else:
            x.parent.right = y

        y.left = x
        x.parent = y
        self.rotations += 1

    def right_rotate(self, x):
        y = x.left
        x.left = y.right

        if y.right != self.NIL:
            y.right.parent = x

        y.parent = x.parent

        if x.parent is None:
            self.root = y
        elif x == x.parent.right:
            x.parent.right = y
        else:
            x.parent.left = y

        y.right = x
        x.parent = y
        self.rotations += 1

    def insert(self, data):
        new_node = Node(data)
        new_node.left = self.NIL
        new_node.right = self.NIL

        parent = None
        current = self.root

        while current != self.NIL:
            parent = current
            if data < current.data:
                current = current.left
            elif data > current.data:
                current = current.right
            else:
                return

        new_node.parent = parent

        if parent is None:
            self.root = new_node
        elif data < parent.data:
            parent.left = new_node
        else:
            parent.right = new_node

        self.fix_insert(new_node)

    def fix_insert(self, node):
        while node.parent and node.parent.color == "RED":
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right

                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.right_rotate(node.parent.parent)

            else:
                uncle = node.parent.parent.left

                if uncle.color == "RED":
                    node.parent.color = "BLACK"
                    uncle.color = "BLACK"
                    node.parent.parent.color = "RED"
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)

                    node.parent.color = "BLACK"
                    node.parent.parent.color = "RED"
                    self.left_rotate(node.parent.parent)

        self.root.color = "BLACK"

    def inorder(self, node):
        if node == self.NIL:
            return []

        return (self.inorder(node.left)
                + [(node.data, node.color)]
                + self.inorder(node.right))

    def height(self, node):
        if node == self.NIL:
            return 0

        return 1 + max(
            self.height(node.left),
            self.height(node.right)
        )


# Experiment
tree = RedBlackTree()

values = [10, 20, 30, 40, 50, 25]

for value in values:
    tree.insert(value)

print("Input values:", values)
print("In-order traversal:", tree.inorder(tree.root))
print("Root:", tree.root.data)
print("Root colour:", tree.root.color)
print("Tree height:", tree.height(tree.root))
print("Total rotations:", tree.rotations)
print("Red-Black Tree experiment completed!")
