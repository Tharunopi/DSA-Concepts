from binary_search_tree import Tree
from level_order import levelOrder

def getVeryLeftNode(root):

    # base case
    if root is None: 
        return
    
    # second base case
    if root.left is None:
        return root
    
    #recursive case 
    return getVeryLeftNode(root.left)

tree = Tree([1, 2, 3, 4, 5, 6])
root = tree.createTree()

print(levelOrder(root))
print(getVeryLeftNode(root))
