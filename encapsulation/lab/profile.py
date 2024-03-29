class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, value):
        if not 5 <= len(value) <= 15:
            raise ValueError("The username must be between 5 and 15 characters.")
        self.__username = value

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, value):
        is_longer_or_equal_to = len(value) >= 8
        is_capital_in_it = [chr for chr in value if chr.isupper()]
        is_digit_in_it = [dig for dig in value if dig.isdigit()]

        if not is_longer_or_equal_to or not is_capital_in_it or not is_digit_in_it:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = value

    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: {"*" * len(self.password)}'

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)
