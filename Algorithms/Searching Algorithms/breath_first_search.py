from collections import deque

class BreathFirstSearch:
    def levelOrder(self, root):
        queue = deque()
        queue.append(root)

        while len(queue) > 0:
            node = queue.popleft()

            print(node.value)

            if node.left is not None:
                queue.append(node.left)

            if node.right is not None:
                queue.append(node.right)