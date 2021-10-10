from authenticator_ import authenticator
from exception import InvalidUsername, PermissionError, NotLoggedInError, NotPermittedError


class Authorizor:
    def __init__(self, authenticator) -> None:
        self.authenticator = authenticator
        self.permissions = {}

    def add_permission(self, perm_name):
        try:
            self.permissions[perm_name]
        except KeyError:
            self.permissions[perm_name] = set()
        else:
            raise PermissionError("Permission Exists.")

    def permit_user(self, perm_name, username):
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission doesn't Exists.")
        else:
            user_perm = self.authenticator.users.get(username)
            if not user_perm:
                raise InvalidUsername(username)
            perm_set.add(username)  # add username into set to avoid add dumplicate username.

    def check_permission(self, perm_name, username):
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            perm_set = self.permissions[perm_name]
        except KeyError:
            raise PermissionError("Permission dose not exist.")
        else:
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                return True


authorizor = Authorizor(authenticator)