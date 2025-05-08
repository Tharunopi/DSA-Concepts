from binary_tree import Tree



def search(root, target):
    if root is not None:
        if search(root.left, target):
            return True

        value = int(root.value)
        if value == target:
            return True

        if search(root.right, target):
            return True

        return False
tree = Tree([1, 2, 3, 4, 5])
root = tree.createTree()

print(search(root=root, target=5))