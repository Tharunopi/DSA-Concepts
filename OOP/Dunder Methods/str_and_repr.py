class Car:
    def __init__(self, make, model, year):
        self.make = make
        self.year = year
        self.model = model

    def __str__(self):
        return f"{self.year} {self.make} {self.model}"
    
    def __repr__(self):
        return f"Car(make='{self.make}', model='{self.model}', year={self.year})"
    
myCar = Car('Toyota', 'Corolla', 2021)

print(str(myCar))
print(repr(myCar))