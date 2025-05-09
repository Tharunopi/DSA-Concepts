from binary_search_tree import Tree, Node
from level_order import levelOrder

def balance(arr):
    if not arr:
        return None

    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = balance(arr[:mid])
    root.right = balance(arr[mid + 1:])

    return root

val = balance([1, 23, 45, 67, 87, 90, 111])

print(levelOrder(val))