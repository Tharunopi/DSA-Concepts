from binary_tree import Tree
from collections import deque

def leftView(root):
    history = []
    queue = deque()
    queue.append((root, 0))

    while len(queue) > 0:
        node, lvl = queue.popleft()
        history.append((node.value, lvl))

        if node.left is not None:
            queue.append((node.left, lvl+1))

        if node.right is not None:
            queue.append((node.right, lvl+1))

    result = {}

    for i in history:
        if f"Level: {i[1]}" not in result.keys() and i[0] is not None:
            result[f"Level: {i[1]}"] = i[0] 

    return result

tree = Tree([1, 2, 3, 4, None, 5, 6, None, None, None, 7])
root = tree.createTree()

print(leftView(root))