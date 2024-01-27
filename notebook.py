import json
from note import Note


class Notebook:
    def __init__(self):
        self.notes = []

    def add_note(self):
        title = input("\nInput title >> ")
        content = input("\nInput content >> ")
        note = Note(title, content)
        self.notes.append(note.to_dict())
        print("\nAdded\n")

    def display_all_notes(self):
        if len(self.notes) == 0:
            print("\nNo notes yet\n")
        else:
            for index, note in enumerate(self.notes):
                print(f"Note {index + 1}:")
                for key, value in note.items():
                    print(f"{key}: {value}")

    def display_note(self):
        title = input("\nInput title of a note >> ")
        for i in self.notes:
            if title in i.keys():
                print(f"\n{title}: {i.get(title)}\n")
                break
        else:
            print("\nNote was not found\n")

    def edit_note(self):
        title = input("\nInput title of a note >> ")
        for i in self.notes:
            if title in i.keys():
                new_key = input("Input new title >> ")
                value = i.pop(title)
                i[new_key] = value
                i[new_key] = input("Input new note >> ")
                print("\nChanged\n")
                break
        else:
            print("\nNote was not found\n")

    def delete_note(self):
        title = input("\nInput title of a note >> ")
        for i in self.notes:
            if title in i.keys():
                self.notes.remove(i)
                print("\nDeleted\n")
                break
        else:
            print("\nNote was not found\n")

    def save_notebook(self):
        file_path = input("Input file name >> ")
        with open(file_path + ".json", 'w') as json_file:
            json.dump(self.notes, json_file)
        print("Saved")

    def load_notebook(self):
        file_path = input("Input file name >> ")
        with open(file_path + ".json", 'r') as json_file:
            self.notes = json.load(json_file)
        print("Loaded")
