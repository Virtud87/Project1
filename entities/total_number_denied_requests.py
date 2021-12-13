class TotalNumberDeniedRequests:
    def __init__(self, employee_id: int, name: str, total_requests_denied: int):
        self.employee_id = employee_id
        self.name = name
        self.total_requests_denied = total_requests_denied

    def create_tndr_dictionary(self):
        return {
            "employeeId": self.employee_id,
            "name": self.name,
            "totalRequestsDenied": self.total_requests_denied
        }
