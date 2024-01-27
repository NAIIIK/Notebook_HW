from menu import Menu


class UI:
    def __init__(self):
        self.menu = Menu()
        self.flag = True
        self.error_text = "Select an available option"

    def start(self):
        print("Welcome!")
        while self.flag:
            self.menu.print_menu()
            self.choice()

    def choice(self):
        try:
            user_input = int(input("\nSelect an option >> "))
            if user_input < 1 or user_input > self.menu.get_size():
                self.error()
            elif user_input == 8:
                self.finish()
            else:
                self.menu.execute(user_input)
        except ValueError:
            self.error()

    def finish(self):
        print("Exiting...")
        self.flag = False

    def error(self):
        print(f"\n{self.error_text}\n")
