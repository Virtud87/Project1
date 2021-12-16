class Credentials:
    def __init__(self, user_name: str, password: str):
        self.user_name = user_name
        self.password = password

    def create_credentials_dictionary(self):
        return {
            "username": self.user_name,
            "password": self.password
        }
