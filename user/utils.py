import hashlib


class PasswordCreator:
    def __init__(self, raw_password: str):
        self.__raw_password = raw_password

    def hash_password(self):
        return hashlib.sha256(self.__raw_password.encode()).hexdigest()

    def check_password_validation(self):
        if type(self.__raw_password) != str:
            raise TypeError('raw password should be str')

        if len(self.__raw_password) < 6:
            raise ValueError("Password must be at least 6 characters long")

        has_big_char = False
        has_small_char = False
        has_digit = False

        for c in self.__raw_password:
            if c.isupper():
                has_big_char = True
            if c.islower():
                has_small_char = True
            if c.isdigit():
                has_digit = True

        if has_digit is False:
            raise ValueError("Password must have at least 1 digit")
        if has_small_char is False:
            raise ValueError("Password must have at least 1 small character")
        if has_big_char is False:
            raise ValueError("Password must have at least 1 capital character")
