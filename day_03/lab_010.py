# Condition

# Check voting eligibility by age
age = int(input("Enter your age: "))

if age > 18:
    print("You're eligible to vote.")
else:
    print("Your age must be 18 or above to vote.")

print("==============================================")

# Find the maximum of three numbers entered by the user using if...elif...else.
# This is an another way to solve the same problem we did in lab_009.py

num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

if num_1 > num_2 and num_1 > num_3:
    print(f"{num_1} is the greatest number")
elif num_2 > num_1 and num_2 > num_3:
    print(f"{num_2} is the greatest number")
else:
    print(f"{num_3} is the greatest number")

print("==============================================")