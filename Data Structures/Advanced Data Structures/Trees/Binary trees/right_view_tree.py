from binary_tree import Tree
from collections import deque

def rightView(root):
    nodeHistory = []
    results = {}

    queue = deque()
    queue.append((root, 0))

    while len(queue) > 0:
        node, lvl = queue.popleft()
        nodeHistory.append((node.value, lvl))

        if node.left is not None:
            queue.append((node.left, lvl+1))

        if node.right is not None:
            queue.append((node.right, lvl+1))

    for i in nodeHistory:
        results[i[1]] = i[0]

    return results

tree = Tree([1, 2, 3, 4, None, 5, 6, None, None, None, 7])
root = tree.createTree()

print(rightView(root))