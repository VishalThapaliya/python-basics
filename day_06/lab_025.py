# Python Exception - (like try-catch in Javascript)
# An exception is Python telling you that something went wrong while the program was running.
# Common exceptions you'll encounter as a beginner include: ValueError — wrong value, TypeError — wrong type, NameError — variable doesn't exist
# IndexError — list index doesn't exist, KeyError — dictionary key doesn't exist, ZeroDivisionError — trying to divide by zero, FileNotFoundError — trying to open a file that doesn't exist
# Python's built-in exception hierarchy includes these and many others.

# Example: 1
try:
    number = int(input("Enter a number: "))
    print("Your number is: ", number)

except:
    print("Please enter a valid number.")


# Example: 2
try:
    number = int(input("Enter a number: "))
    print(10 / number)
except:
    print("Something went wrong.")


# Catch specific exceptions - This is better than using a completely generic except.
# try       → try this
# except    → something went wrong
# else      → everything worked
# finally   → do this no matter what

try:
    number = int(input("Enter a number: "))
    result = 10 / number
    print(result)

except ValueError:
    print("Please enter a number.")

except ZeroDivisionError:
    print("You cannot divide by zero.")

else:
    print("You entered: ", number)

finally:
    print("Program finished.")
