# Functions

# simple function
def greet():
    print("Hello from a function.")

greet()

# Function with an argument
def new_greet(name):
    print(f"Hello {name}")

new_greet("Bishal")


# Function with two arguments
def get_full_name(first_name, last_name):
    print(f"Your first name is {first_name} and last name is {last_name}")

get_full_name("Bishal", "Thapaliya")


# Function with Arbitrary Arguments (*args)
# Arbitrary arguments = unlimited number of arguments
def show_children(*children):
    print("1st Child: ", children[0])
    print("2nd Child: ", children[1])
    print("3rd Child: ", children[2])
    print("4th Child: ", children[3])

show_children("Shriyank", "Riaan", "Prayusha", "Niaara")

# Keyword Arguments
def get_youngest_child(child1, child2, child3):
    print(f"Your youngest child is: {child3}")

get_youngest_child("Shriyank", "Riaan", "Prayusha")

# Arbitrary Keyword Arguments (**kwargs)
def show_details(**details):
    print("First name: ", details["first_name"])
    print("Last name: ", details["last_name"])

show_details(first_name="Bishal", last_name="Thapaliya", city="Grenoble", country="France")

# Default Paramter value
def guess_country(country= "Nepal"):
    print("I am from " + country)

guess_country()
guess_country("France")

# Return function
def get_sum(a, b):
    return a + b

result = get_sum(4, 5)
print(result)