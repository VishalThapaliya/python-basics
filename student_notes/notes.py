def add_note(note):
    with open("notes.txt", "a") as file:
        file.write(note + "\n")

def show_notes():
    with open("notes.txt", "r") as file:
        return file.read()