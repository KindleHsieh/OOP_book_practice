from exception import (UsernameAlreadyExists, PasswordTooShort,
InvalidUsername, InvalidPassword)
from user import User

class Authenticator:
    def __init__(self) -> None:
        self.users = {}

    def add_user(self, username, password):
        if username in self.users:
            raise UsernameAlreadyExists(username)
        
        if len(password) < 6:
            raise PasswordTooShort(username)
        
        self.users[username] = User(username, password)

    def login(self, username, password):
        user = self.users.get(username)
        if not user:
            raise InvalidUsername(username)
        
        if not user.check_password(password):
            raise InvalidPassword(username, password)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        if username in self.users:
            return self.users[username].is_logged_in
        return False

authenticator = Authenticator()