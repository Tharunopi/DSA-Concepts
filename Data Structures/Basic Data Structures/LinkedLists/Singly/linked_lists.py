class Node:
    def __init__(self, head, next=None):
        self.head = head
        self.next = next
    
class LinkedLists:
    def __init__(self):
        pass

    def add_begning(self, value, old_node=None):
        if old_node is None:
            return Node(value)
        return Node(value, next=old_node)
    
    def add_back(self, value, old_node=None):
        if old_node is None:
            return Node(value)
        new_node = Node(value)
        cur = old_node
        while cur:
            cur = cur.next
        cur.next = new_node
        return old_node
    
    def display(self):
        pass