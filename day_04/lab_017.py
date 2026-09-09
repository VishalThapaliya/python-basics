# Set (like in JS)
# A set is an unordered collection of unique items
# Sets are mutable but do not allow duplicate elements.

fruits = {"apple", "banana", "cherry"}
fruits.add("orange")
print(fruits)

fruits.remove("banana")
print(fruits)

print("apple" in fruits)
print("banana" in fruits)

# Will not add "apple" to the list as it will be a duplicate value
fruits.add("apple")
print(fruits)

# Set Union
set1 = {1, 2, 3}
set2 = {3, 4, 5, 6}

# Union
print("Union: ", set1 | set2)

# Intersection
print("Intersection: ", set1 & set2)

# Division
print("Division: ", set1 - set2)
print("Division: ", set2 - set1)
print("Symmetric Division: ",set1 ^ set2)
