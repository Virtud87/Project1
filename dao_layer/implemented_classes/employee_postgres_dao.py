from typing import List

from dao_layer.abstract_classes.employee_dao import EmployeeDAO
from entities.reimbursement import Reimbursement


class EmployeePostgresDAO(EmployeeDAO):
    def login(self, user_name: str, password: str) -> bool:
        pass

    def submit_new_request(self, date: str, amount: float, reason: str) -> bool:
        pass

    def view_requests_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        pass

    def logout(self) -> bool:
        pass
