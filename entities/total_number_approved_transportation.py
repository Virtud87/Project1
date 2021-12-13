class TotalNumberApprovedTransportation:
    def __init__(self, employee_id: int, name: str, total_transportation_requests: int):
        self.employee_id = employee_id
        self.name = name
        self.total_transportation_requests = total_transportation_requests

    def create_tnat_dictionary(self):
        return {
            "employeeId": self.employee_id,
            "name": self.name,
            "totalTransportationRequests": self.total_transportation_requests
        }
