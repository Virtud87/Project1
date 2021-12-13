class TotalAmountApproved:
    def __init__(self, employee_id: int, name: str, total_amount: float):
        self.employee_id = employee_id
        self.name = name
        self.total_amount = total_amount

    def create_tap_dictionary(self):
        return {
            "employeeId": self.employee_id,
            "name": self.name,
            "totalAmount": self.total_amount
        }
