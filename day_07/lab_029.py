# Challenge
# Create a simple notes application:
#
# 1. Add note
# 2. View notes
# 3. Exit
#
# When the user chooses 1, save the note to:
#
# notes.txt
#
# When they choose 2, read and display the notes.

while True:

    user_input = int(input("Enter your number between 1: Add note; 2: View notes; and 3: Exit - "))

    if user_input == 1:
        note = input("Enter your note: ")

        with open("notes.txt", "a") as file:
            file.write(note + "\n")
    elif user_input == 2:
        with open("notes.txt", "r") as file:
            for line in file:
                print(line.strip())
    elif user_input == 3:
        break

    else:
        print("Invalid choice")