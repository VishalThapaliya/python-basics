# Class with Constructor

class Car:

    # Constructor
    def __init__(self, brand, model, year):
        # self === 'this' in javascript
        self.brand = brand
        self.model = model
        self.year = year

    def display_info(self):
        return f"This is a {self.brand} {self.model} of the year {self.year}"

# Creating a Car object
my_car = Car("Peugeot", "3008", 2026)
print(my_car.display_info())