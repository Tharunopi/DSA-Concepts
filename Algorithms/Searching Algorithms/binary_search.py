class BinarySearch:

    def searchRecursive(self, x, target):
        if len(x) <= 0:
            return False
        
        mid = len(x) // 2

        if x[mid] == target:
            return True

        if x[mid] > target:
            return self.search(x[:mid], target)
        
        if x[mid] <= target:
            return self.search(x[mid+1:], target)
        
    def searchIterative(self, x, target):
        curLen = len(x)

        while curLen > 0:
            mid = len(x) // 2

            if x[mid] == target:
                return True

            elif x[mid] > target:
                x = x[:mid]
                curLen = len(x)

            else:
                x = x[mid+1:]
                curLen = len(x)

        return False
        
a = BinarySearch()
print(a.searchIterative([1, 2, 3, 4, 5], 6))