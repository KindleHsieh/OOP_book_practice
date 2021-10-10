import sys
from notebook import Note, Notebook


class Menu:
    def __init__(self):
        self.notebook = Notebook()
        self.choices = {
            "1": self.show_notes,
            "2": self.search_notes,
            "3": self.modify_note,
            "4": self.quit
        }
        print("Use run method to start system.")
    
    def run(self):
        while True:
            choice = input("Enter an option: ")
            action = self.choices.get(choice)

            if action:
                action()
            else:
                print('No this channel.')

    def show_notes(self):
        