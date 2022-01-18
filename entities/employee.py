class Employee:
    def __init__(self, employee_id: int, manager: int, first_name: str, last_name: str, user_name: str, password: str):
        self.employee_id = employee_id
        self.manager = manager
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password
