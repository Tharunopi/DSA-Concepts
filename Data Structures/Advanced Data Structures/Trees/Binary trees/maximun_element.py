from binary_tree import Tree
from traversal_binary_tree import Traversal

class Maximum:

    @staticmethod
    def getMax(root):

        if root is not None:
            Maximum.getmax(root.left)