class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left 
        self.right = right

    def __str__(self):
        return f"{self.value}"

class Tree:
    def __init__(self, values=None):

        if values is None:
            self.values = []

        else:
            assert isinstance(values, list)
            self.values = values

    def createTree(self) -> Node:
        try:

            if len(self.values) == 0:
                raise IndexError

            nodes = [Node(i) for i in self.values]
            nodesLen = len(nodes)

            for i in range(nodesLen):
                leftNode = (2 * i) + 1
                rightNode = (2 * i) + 2

                if leftNode < nodesLen:
                    nodes[i].left = nodes[leftNode]

                if rightNode < nodesLen:
                    nodes[i].right = nodes[rightNode]

            return nodes[0]
        
        except IndexError as e:
            print(e)

tree = Tree([1, 2, 3, 4])
root = tree.createTree()
print(root.value)
print(root.left)