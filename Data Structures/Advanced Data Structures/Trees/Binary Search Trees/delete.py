from binary_search_tree import Tree
from collections import deque
from level_order import levelOrder

def delete(root, target):
    if root is None:
        return 
    
    # case-1 node has no child

    if root:
        pass