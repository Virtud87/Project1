from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class EmployeeDAO(ABC):
    @abstractmethod
    def login(self, user_name: str, password: str) -> bool:
        pass

    @abstractmethod
    def submit_new_request(self, date: str, amount: float, reason: str) -> bool:
        pass

    @abstractmethod
    def view_requests_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def logout(self) -> bool:
        pass
