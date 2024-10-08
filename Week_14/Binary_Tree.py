class Node:
    data = int
    next = "Node"

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_data):
        self.root = Node(root_data)

    def insert(self, data):
        self._insert_recursive(self.root, data)

    
    def _insert_recursive(self, current_node, data):
        if data < current_node.data:
            if current_node.left is None:
                current_node.left = Node(data)
            else: 
                self._insert_recursive(current_node.left, data)

        else: 
            if current_node.right is None:
                current_node.right = Node(data)
            else: 
                self._insert_recursive(current_node.right, data)       

    def print_tree(self):
        self._print_in_order(self.root)

    def _print_in_order(self, current_node):
        if current_node is not None:
            self._print_in_order(current_node.left)
            print(current_node.data)
            self._print_in_order(current_node.right)

binary_tree = BinaryTree(10)  # Create the tree with root node 10

# Insert nodes
binary_tree.insert(5)
binary_tree.insert(15)
binary_tree.insert(3)
binary_tree.insert(7)
binary_tree.insert(12)
binary_tree.insert(17)

# Print the binary tree using in-order traversal
print("Binary Tree (In-Order Traversal):")
binary_tree.print_tree()