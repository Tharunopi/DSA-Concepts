from binary_search_tree import Tree
from collections import deque
from level_order import levelOrder

def searchRecursive(root, target):
    if root is None:
        return False
    
    if root.value == target:
        return True
    
    if target < root.value:
        return searchRecursive(root.left, target)

    else:
        return searchRecursive(root.right, target)



def searchIterative(root, target):
    queue = deque()
    queue.append(root)

    while len(queue) > 0:
        node = queue.popleft()
        if node.value == target:
            return True
        
        if node.left is not None:
            queue.append(node.left)

        if node.right is not None:
            queue.append(node.right)

    return False

tree = Tree([1, 2, 3, 4, 5, None, 6, None, None, None, None, 7])
root = tree.createTree()

print(searchRecursive(root, 5))