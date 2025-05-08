from binary_tree import Tree
from collections import deque

def height(root):
    if root is None:
        return 0
    
    leftHeight = height(root.left)
    print(leftHeight, root)
    rightHeight = height(root.right)
    print(rightHeight, root)

    return 1 + max(leftHeight, rightHeight)

def height_iterative(root):
    queue = deque([root])
    print(queue)

tree = Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
root = tree.createTree()

print(height_iterative(root))