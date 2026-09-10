# Inheritence

# Class 1 : Animal
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass # pass here means skip for the moment, we will implement it later

##########################
# Class 2 : Dog
class Dog(Animal):  # Dog class in inheriting Animal class
    def speak(self):
        return f"{self.name} says Woof!"

#########################
# Class 3 : Cat
class Cat(Animal):  # Dog class in inheriting Animal class
    def speak(self):
        return f"{self.name} says Myau-Myau!"

#########################
# Creating object
dog = Dog("Jacky")
print(dog.speak())

cat = Cat("Pussy")
print(cat.speak())
