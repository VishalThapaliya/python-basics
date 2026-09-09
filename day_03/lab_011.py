# Loops

# For loop
for i in range(0, 10):
    print(f"{i}: Hello Python")

print("==========================================================")

for i in range(1, 10, 2): # output: 1-9; 1 = starting point; 10 = ending point; 2 = intervals in between
    print(i)

print("==========================================================")

# Break the loop at a specific point. e.g. when the counter reaches at 5, break the program
for counter in range(0, 100):
    print(counter)
    if counter == 5:
        break
print("End of program")

print("==========================================================")

# Skip a particular point. e.g. skip the counter 5 and pass it to the next counting number
for counter in range(10):
    if counter == 5:
        pass
    else:
        print(counter)

print("==========================================================")

# While loop

i = 0
while i < 5:
    print(i)
    i += 1

print("==========================================================")