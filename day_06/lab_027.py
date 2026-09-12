# File I/O -> reading and writing files

# open hello.txt using write mode
file = open("hello.txt", "w")
file.write("Hello, I am learning Python.")
file.close()

# Read a file
file = open("hello.txt", "r")
content = file.read()
print(content)
file.close()

# The better way: with | Python automatically handles closing the file when the with block finishes.
# Read file using 'with'
with open("hello.txt", "r") as file:
    content = file.read()

print(content + " using With")

# Write using 'with'
with open("hello.txt", "w") as file:
    file.write("I am learning Python to master QA Automation")

# Append
with open("hello.txt", "a") as file:
    file.write("\nI am learning Python to master QA Automation Testing")
