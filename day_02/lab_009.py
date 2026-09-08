# Use the ternary operator to find the maximum of three numbers entered by the user.
num_1 = int(input("Enter first number: "))
num_2 = int(input("Enter second number: "))
num_3 = int(input("Enter third number: "))

print(
    f"{num_1} is maximum"
    if num_1 > num_2 and num_1 > num_3
    else (
        f"{num_2} is maximum"
        if num_2 > num_1 and num_2 > num_3
        else f"{num_3} is maximum"
    )
)