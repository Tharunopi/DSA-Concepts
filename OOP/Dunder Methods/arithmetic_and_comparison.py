class InventoryItem:
    def __init__(self, name, qty):
        self.name = name
        self.qty = qty

    def __str__(self):
        return f"{self.name} {self.qty}"
    
    #arithmetic operators 
    def __add__(self, other):
        if isinstance(other, InventoryItem) and other.name == self.name:
            return InventoryItem(self.name, self.qty + other.qty)
        
    def __sub__(self, other):
        if isinstance(other, InventoryItem) and other.name == self.name:
            if self.qty >= other.qty:
                return InventoryItem(self.name, self.qty - other.qty)
            
    def __mul__(self, other):
        if isinstance(other,(int, float)):
            return InventoryItem(self.name, self.qty * other)
        
    def __truediv__(self, other):
        if isinstance(other, (int, float)) and other != 0:
            return InventoryItem(self.name, self.qty / other)
        
    # comparison operator 
    def __eq__(self, other):
        if isinstance(other, InventoryItem):
            return self.name == other.name and self.qty == other.qty
        
    def __lt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.qty < other.qty
        
    def __gt__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.qty > other.qty
        
    def __lte__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.qty <= other.qty
        
    def __gte__(self, other):
        if isinstance(other, InventoryItem) and self.name == other.name:
            return self.qty >= other.qty

one = InventoryItem('S23', 4)
two = InventoryItem('S23', 6)

print(one >= two)