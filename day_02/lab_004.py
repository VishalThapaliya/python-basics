# String functions

my_str = "I am learning Python"

# String slicing
print(my_str[0: 10]) # 0 = starting point, 10 = how many characters

# String length
print(len(my_str))

# Show string from a specific point
print(my_str[8:len(my_str)])

# Reverse a string
print(my_str[::-1])

# String concatenate
str_1 = "I am learning "
str_2 = "Python for QA Automation"
str_3 = str_1 + str_2
print(str_3)

# String concatenate with number
num = 1.0
str_4 = str(num) + " " + str_3
print(str_4)