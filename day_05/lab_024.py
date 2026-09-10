# Multi-level Inheritance

# Class 1 : Grand Father
class GrandFather:
    def house(self):
        print("3BHK House")

    def car(self):
        print("Renault Captur 2026 Model")

# Class 2 : Father inherits from GrandFather
class Father(GrandFather):
    def house(self):
        print("4BHK Apartment")

# Class 3 : Son inherits from Father that give access to GrandFather also
class Son(Father):
    pass


# Creating Object
s = Son()
s.house() #Inherited/overridden from Father as priority
s.car() # Inherited from GrandFather

# Son gets house() from Father and car() from GrandFather.


