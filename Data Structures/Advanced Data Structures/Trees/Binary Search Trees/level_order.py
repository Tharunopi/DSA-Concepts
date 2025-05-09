from binary_search_tree import Tree
from collections import deque

def levelOrder(root):
    nodeHistory = []
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()
        nodeHistory.append(node.value)

        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return nodeHistory