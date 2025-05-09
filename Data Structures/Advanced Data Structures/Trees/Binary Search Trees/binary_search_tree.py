class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def __str__(self):
        return f"{self.value}"
    
class Tree:
    def __init__(self, values: list):
        self.values = values 

    def createTree(self):

        try:
            if len(self.values) <= 0:
                raise IndexError
            nodes = [Node(i) for i in self.values]

            for i in range(len(nodes)):
                leftNode = (2 * i) + 1
                rightNode = (2 * i) + 2

                if leftNode < len(self.values):
                    nodes[i].left = nodes[leftNode]

                if rightNode < len(self.values):
                    nodes[i].right = nodes[rightNode]

            return nodes[0]

        except IndexError as e:
            print(e)