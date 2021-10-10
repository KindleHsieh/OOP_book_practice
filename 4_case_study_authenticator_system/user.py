"""
for create a user by username and password.
also this class will check password.
"""
import hashlib

class User:
    def __init__(self, username, password) -> None:
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password: str) -> str:
        """username + password for """

        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password

