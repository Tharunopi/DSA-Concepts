from binary_search_tree import Tree
from level_order import levelOrder

tree = Tree([1, 2, 3, 4, 5, 6])
root = tree.createTree()

print(levelOrder(root))
