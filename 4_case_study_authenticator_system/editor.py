from authenticator_ import authenticator
from authorizor import authorizor
from exception import (InvalidUsername, InvalidPassword,
NotLoggedInError, NotPermittedError)


class Editor:
    def __init__(self):
        self.username = None
        self.menu_map = {
            "login": self.login,
            "test": self.test,
            "change": self.change,
            "quit": self.quit
        }
    
    def login(self):
        logged_in = False
        while not logged_in:
            username = input("Username:")
            password = input("Password:")

            try:
                logged_in = authenticator.login(username, password)
            except InvalidUsername:
                print("That username doesn't exist.")
            except InvalidPassword:
                print("Incorrect Password.")
            else:
                self.username = username
    
    def is_permitted(self, permission):
        try:
            authorizor.check_permission(permission, self.username)
        except NotLoggedInError as e:
            print(f"{e.username} is not logged in.")
            return False
        except NotPermittedError as e:
            return False
        else:
            return True

    def test(self):
        if self.is_permitted("test program"):
            print("Testing program now...")

    def change(self):
        if self.is_permitted("change program"):
            print("Changing program now...")

    def quit(self):
        raise SystemError

    def menu(self):
        try:
            answer = ''
            while True:
                print(f"Please Enter one of the work{self.menu_map.keys()}")
                answer = input("").lower()
                try:
                    func = self.menu_map[answer]
                
                except KeyError:
                    print('{answer} is not a valid option.')
                    func = self.menu
                else:
                    func()
        finally:
            print('Thank you.')