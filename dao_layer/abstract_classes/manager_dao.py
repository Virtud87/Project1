from abc import ABC, abstractmethod
from typing import List

from entities.reimbursement import Reimbursement


class ManagerDAO(ABC):
    @abstractmethod
    def login(self, user_name: str, password: str) -> bool:
        pass

    @abstractmethod
    def approve_reimbursement_by_id(self, reimbursement_id: int) -> bool:
        pass

    @abstractmethod
    def deny_reimbursement_by_id(self, reimbursement_id: int) -> bool:
        pass

    @abstractmethod
    def decision_comment_by_id(self, reimbursement: Reimbursement) -> bool:
        pass

    @abstractmethod
    def view_pending_requests(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def view_past_requests(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def view_stats(self) -> List:
        pass

    @abstractmethod
    def logout(self) -> bool:
        pass
