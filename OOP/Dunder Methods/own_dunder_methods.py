class Counter:

    def __init__(self):
        self.value = 1

    def countUp(self):
        self.value += 1

    def countDown(self):
        self.value -= 1

    def __str__(self):
        return str(self.value)
    
    def __add__(self, other):
        if isinstance(other, Counter):
            return self.value + other.value

count1 = Counter()
count2 = Counter()

count1.countUp()
count2.countUp()

print(count1, count2)
print(count1 + count2)