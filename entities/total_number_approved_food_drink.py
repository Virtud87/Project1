class TotalNumberApprovedFoodDrink:
    def __init__(self, employee_id: int, name: str, total_food_drink_requests: int):
        self.employee_id = employee_id
        self.name = name
        self.total_food_drink_requests = total_food_drink_requests

    def create_tnafd_dictionary(self):
        return {
            "employeeId": self.employee_id,
            "name": self.name,
            "totalFoodDrinkRequests": self.total_food_drink_requests
        }
