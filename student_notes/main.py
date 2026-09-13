import notes

while True:
    print("\nStudent Notes App")
    print("1. Add note")
    print("2. View notes")
    print("3. Exit")

    choice = int(input("Choose an option: "))

    if choice == 1:
        note = input("Enter a note: ")
        notes.add_note(note)

        print("Note saved.")

    elif choice == 2:
        print("\nYour Notes: ")
        print(notes.show_notes())

    elif choice == 3:
        break

    else:
        print("Invalid choice")