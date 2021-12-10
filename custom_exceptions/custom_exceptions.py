class UsernameOrPasswordIncorrect(Exception):
    def __init__(self, message):
        self.message = message


class NegativeDollarAmount(Exception):
    def __init__(self, message):
        self.message = message


class NonNumericAmount(Exception):
    def __init__(self, message):
        self.message = message
