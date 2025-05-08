from binary_tree import Tree
from traversal_binary_tree import Traversal

tree = Tree([2, 3, 4, None, None, None, 5, 6])
root = tree.createTree()

looper = Traversal()
looper.inorder(node=root)