from binary_tree import Tree
from collections import deque

def levelOrder(root):
    
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()

        print(node)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

tree = Tree([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
root = tree.createTree()

levelOrder(root)