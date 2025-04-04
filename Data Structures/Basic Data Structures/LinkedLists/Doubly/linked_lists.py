class Node:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev 
        self.next = next

def add(value, old_node=None):
    if old_node:
        new_node = Node(value, next=old_node)
        old_node.prev = new_node
    else:
        new_node = Node(value)
    return new_node
    
def show(node, mode=None):
    if mode == 'f':
        cur = node
        while cur:
            print(cur.value)
            cur = cur.prev
    if mode == 'b' or mode == None:
        cur = node
        while cur:
            print(cur.value)
            cur = cur.next

def remove(node, value):
    cur = node
    if cur.value == value:
        return cur.next
    while cur:
        if cur.value == value:
            if cur.prev:
                cur.prev.next = cur.next
            if cur.next:
                cur.next.prev = cur.prev

        cur = cur.next
    return node

a = add(1)
b = add(2, a)
c = add(3, b)
# show(a, 'f')
d = remove(c, 1)
show(d)