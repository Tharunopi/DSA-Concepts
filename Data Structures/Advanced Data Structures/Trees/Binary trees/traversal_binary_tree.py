from binary_tree import Tree

class Traversal:
    def __init__(self):
        pass

    def inorder(self, node):

        if node is not None:
            self.inorder(node.left)
            print(node.value)
            self.inorder(node.right)
