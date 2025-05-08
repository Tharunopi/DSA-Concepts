from binary_tree import Tree

class Maximum:
    def __init__(self):
        self.value = None

    def getMax(self, root):

        if root is not None:
            self.getMax(root.left)

            valued = root.value

            if self.value is None:
                self.value = valued
            
            elif valued > self.value:
                self.value = valued

            self.getMax(root.right)

tree = Tree([1, 2, 3, 4, 5, 785, 6, 7])
root = tree.createTree()

maxi = Maximum()
maxi.getMax(root)

print(maxi.value)