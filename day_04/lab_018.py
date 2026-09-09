# Tuple
# A Tuple is an ordered collection of items which can be of any type
# Tuples are immutable, meaning their elements cannot be changed after tuple is created
# Tuple is like a list, but contains values in between parenthesis "(" ")"

fruits =("apple", "banana", "cherry")
print(fruits[1]) # Output: banana

# You cannot update tuple value like
# fruits[1] = "blueberry"

# Dictionary
# A dictionary is an unordered collection of key-value pairs

student = { "name": "Bishal", "age": 25, "courses": ["Python", "Robot Framework", "Playwright"]}
print(student["name"])
print(student["age"])
print(student)