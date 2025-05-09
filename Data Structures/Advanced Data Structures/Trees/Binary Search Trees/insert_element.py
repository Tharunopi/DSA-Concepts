from binary_search_tree import Tree, Node
from level_order import levelOrder
from collections import deque

def insert(root, value):
    if root is None:
        return Node(value)
    
    if value < root.value:
        root.left = insert(root.left, value)

    elif value > root.value:
        root.right = insert(root.right, value)

    return root


tree = Tree([1, 2, 3, 4, 5, None, 6, None, None, None, None, 7])
root = tree.createTree()

print(levelOrder(root))

root2 = insert(root, 8)

print(levelOrder(root))