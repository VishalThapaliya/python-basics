# Write a Python program to calculate the area of a circle given its radius using the formula area=π×r^2 ( Take pie as 3.14)
radius = int(input("Enter radius value : "))
pi = 3.14

# area = pi*r2
area = pi * (radius ** 2)
print(area)