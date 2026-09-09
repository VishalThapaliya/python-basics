# Triangle Classifier
# side1 == side2 == side3 -> Equilateral
# side1 == side2 or side2 == side3 or side1 == side3 -> Isosceles
# else -> Scalene

print("Triangle Classifier")
side1 = float(input("Enter value for side 1: "))
side2 = float(input("Enter value for side 2: "))
side3 = float(input("Enter value for side 3: "))

if side1 == side2 == side3:
    print("Equilateral")
elif side1 == side2 or side2 == side3 or side1 == side3:
    print("Isosceles")
else:
    print("Scalene")

# ====================================================================
print("====================================================================")

# Factorial
# n = 5;        n = 3
# 5*4*3*2*1 = 120;      3*2*1 = 6
print("Factorial of a number")
number = int(input("Enter a number : "))

fact = 1
if number <= 0:
    print(f"Factorial of {number} = ", fact)
else:
    for i in range(1, number + 1):
        fact = fact * i
    print(f"Factorial of {number} = ", fact)
