from binary_tree import Tree
from collections import deque

def levelOrder(root):
    nodeHistory = []
    queue = deque()
    queue.append(root)

    while len(queue) > 0:

        node = queue.popleft()

        # print(node)
        nodeHistory.append(node.value)

        if node.left is not None:
            queue.append(node.left)

        if  node.right is not None:
            queue.append(node.right)

    return nodeHistory

tree = Tree([2, 3, 4, None, None, None, 5, 6])
root = tree.createTree()

nodes = levelOrder(root)
print(nodes[-1])