# Modules --> splitting/reusing Python code. A Python file containing reusable code can be used as a module.

# Modules
import calculator

print(calculator.add(10, 5))
print(calculator.subtract(10, 5))
print(calculator.multiply(10, 5))
print(calculator.division(10,5))

print("------------------------------------")
# import specific functions
from calculator import add, subtract
print(add(15, 10))
print(subtract(15, 12))