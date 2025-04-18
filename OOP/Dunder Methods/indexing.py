class LinkedLists:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next
        self.size = 1

    def __str__(self):
        values = []
        cur = self
        while cur:
            values.append(str(cur.value))
            cur = cur.next 
        return " -> ".join(values)
    
    def 
    
a = LinkedLists(1)
b = LinkedLists(2)
c = LinkedLists(3)
d = LinkedLists(4)
a.next = b
b.next = c
c.next = d

print(a)