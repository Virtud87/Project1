from abc import ABC, abstractmethod
from typing import List

from entities.credentials import Credentials
from entities.reimbursement import Reimbursement
from entities.submission import Submission


class EmployeeService(ABC):
    @abstractmethod
    def service_login(self, credentials: Credentials):
        pass

    @abstractmethod
    def service_submit_new_request(self, submission: Submission):
        pass

    @abstractmethod
    def service_view_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        pass

    @abstractmethod
    def service_logout(self) -> bool:
        pass
