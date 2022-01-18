from abc import ABC, abstractmethod
from typing import List
from entities.reimbursement import Reimbursement


class EmployeeService(ABC):
    @abstractmethod
    def service_employee_login(self, user_name: str, password: str):
        pass

    @abstractmethod
    def service_submit_new_request(self, employee_id, date, amount, reason):
        pass

    @abstractmethod
    def service_view_reimbursements_by_employee_id(self, validated) -> List[Reimbursement]:
        pass
