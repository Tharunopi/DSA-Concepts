from binary_tree import Tree

class Search:
    @staticmethod

    def search(root, target):
        if root is not None:
            Search.search(root.left, target)

            value = int(root.value)
            print(value, target)
            if value == target:
                return True

            Search.search(root.right, target)

        return False

tree = Tree([1, 2, 3, 4, 5])
root = tree.createTree()

print(Search.search(root=root, target=3))