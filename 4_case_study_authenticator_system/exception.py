class AuthException(Exception):
    def __init__(self, username, user=None) -> None:

        self.username = username
        self.user = user

class UsernameAlreadyExists(AuthException):
    pass

class PasswordTooShort(AuthException):
    pass

class InvalidUsername(AuthException):
    pass

class InvalidPassword(AuthException):
    pass

class PermissionError(Exception):
    pass

class NotLoggedInError(AuthException):
    pass

class NotPermittedError(AuthException):
    pass

if __name__ == "__main__":
    try:
        raise Exception("sfsf", "sfjlsf")
    except Exception as e:
        print(e)