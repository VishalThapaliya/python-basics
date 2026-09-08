# Ternary operator
x = 30
y = 50

# "a if condition else b"
print("x is greater" if x > y else "y is greater")


# Create a program that takes two numbers as input and
# prints whether the first number is greater than, less than, or equal to the second number.

first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

print(
    f"{first_number} is greater than {second_number}"
    if first_number > second_number
    else (
        f"{first_number} is less than {second_number}"
        if first_number < second_number
        else f"{first_number} is equal to {second_number}"
    )
)