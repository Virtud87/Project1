class TotalNumberApprovedRequests:
    def __init__(self, employee_id: int, name: str, total_requests_approved: int):
        self.employee_id = employee_id
        self.name = name
        self.total_requests_approved = total_requests_approved

    def create_tnar_dictionary(self):
        return {
            "employeeId": self.employee_id,
            "name": self.name,
            "totalRequestsApproved": self.total_requests_approved
        }
