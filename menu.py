from notebook import Notebook


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.commands = []
        self.commands.append("Add note")
        self.commands.append("Display certain note")
        self.commands.append("Display all notes")
        self.commands.append("Edit note")
        self.commands.append("Delete note")
        self.commands.append("Save notes")
        self.commands.append("Load notes")
        self.commands.append("Exit")

    def print_menu(self):
        for index, command in enumerate(self.commands):
            print(f"{index + 1}. {self.commands[index]}")

    def get_size(self):
        return len(self.commands)

    def execute(self, choice):
        if choice == 1:
            self.notebook.add_note()
        elif choice == 2:
            self.notebook.display_note()
        elif choice == 3:
            self.notebook.display_all_notes()
        elif choice == 4:
            self.notebook.edit_note()
        elif choice == 5:
            self.notebook.delete_note()
        elif choice == 6:
            self.notebook.save_notebook()
        elif choice == 7:
            self.notebook.load_notebook()
