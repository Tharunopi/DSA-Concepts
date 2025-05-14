class DepthFirstSearch:
    def inOrder(self, root):
        if root is None:
            return

        self.inorder(root.left)

        print(root.value)

        self.inorder(root.right)

    def preOrder(self, root):
        if root is None:
            return
        
        print(root.value)

        self.preOrder(root.left)

        self.preOrder(root.right)
        