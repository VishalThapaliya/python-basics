# Get user input and calculate them

num_1 = input("Enter first number: ")
num_2 = input("Enter second number: ")

# simple calculation
addition = int(num_1) + int(num_2)
substraction = int(num_1) - int(num_2)
multiplication = int(num_1) * int(num_2)
division = float(num_1) / float(num_2)

print(f"{num_1} + {num_2} = {addition}")
print(f"{num_1} - {num_2} = {substraction}")
print(f"{num_1} * {num_2} = {multiplication}")
print(f"{num_1} / {num_2} = {division}")