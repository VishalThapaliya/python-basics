# Triangle Classifier
# side1 == side2 == side3 -> Equilateral
# side1 == side2 or side2 == side3 or side1 == side3 -> Isosceles
# else -> Scalene

side1 = float(input("Enter value for side 1: "))
side2 = float(input("Enter value for side 2: "))
side3 = float(input("Enter value for side 3: "))

if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles")
else:
    print("Scalene")