from abc import ABC, abstractmethod
from typing import List
from entities.credentials import Credentials
from entities.reimbursement import Reimbursement


class EmployeeDAO(ABC):
    @abstractmethod
    def get_all_employees(self):
        pass

    @abstractmethod
    def employee_login(self, user_name: str, password: str):
        pass

    @abstractmethod
    def return_employee_id(self, credentials: Credentials):
        pass

    @abstractmethod
    def submit_new_request(self, employee_id, date, amount, reason):
        pass

    @abstractmethod
    def view_reimbursements_by_employee_id(self, validated) -> List[Reimbursement]:
        pass
