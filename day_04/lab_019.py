# Python Lambda
# A lambda function is a small anonymous function
# lambda arguments : expression

add = lambda num: num + 10
print(add(5))


multiply = lambda a, b : a * b
print(multiply(5, 6))

sum = lambda a,b,c: a + b + c
print(sum(5,6,7))

print("==========================================")
#=========================================
#Recursion - a function that calls itself

def rec_count(number):
    print(number)
    if(number == 0):
        return 0
    else:
        rec_count(number - 1)

rec_count(5)

print("==========================================")
def factorial(num):
    if num == 1:
        return 1
    else:
        return num * factorial(num - 1)

print(factorial(5))