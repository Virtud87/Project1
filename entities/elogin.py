class EmployeeLogin:
    def __init__(self, user_name: str, password: str):
        self.employee_id = 0
        self.user_name = user_name
        self.password = password

    def __str__(self):
        return f"id: {self.employee_id}, user_name: {self.user_name}, password: ********"

    def manager_login_to_dictionary(self):
        return {
            "manager_id": self.employee_id,
            "user_name": self.user_name,
            "password": self.password
        }