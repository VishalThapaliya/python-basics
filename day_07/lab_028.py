# Read "student.txt" file and print it

# Read a file
file = open("student.txt", "r")
content = file.read()
print(content)

print("============================")

# Read file line by line
with open("student.txt", "r") as file:
    for line in file:
        print(line.strip())

print("============================")
