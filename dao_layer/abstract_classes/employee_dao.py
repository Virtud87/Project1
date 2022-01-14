from abc import ABC, abstractmethod
from typing import List

from entities.credentials import Credentials
from entities.reimbursement import Reimbursement
from entities.submission import Submission


class EmployeeDAO(ABC):
    @abstractmethod
    def employee_login(self, user_name: str, password: str):
        pass

    @abstractmethod
    def return_employee_id(self, credentials: Credentials):
        pass

    @abstractmethod
    def submit_new_request(self, submission: Submission):
        pass

    @abstractmethod
    def view_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        pass
