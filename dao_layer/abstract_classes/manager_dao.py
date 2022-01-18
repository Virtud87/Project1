from abc import ABC, abstractmethod
from typing import List
from entities.reimbursement import Reimbursement
from entities.total_amount_approved import TotalAmountApproved
from entities.total_number_approved_food_drink import TotalNumberApprovedFoodDrink
from entities.total_number_approved_requests import TotalNumberApprovedRequests
from entities.total_number_approved_transportation import TotalNumberApprovedTransportation
from entities.total_number_denied_requests import TotalNumberDeniedRequests


class ManagerDAO(ABC):
    @abstractmethod
    def get_all_managers(self):
        pass

    @abstractmethod
    def manager_login(self, user_name: str, password: str):
        pass

    @abstractmethod
    def return_manager_id(self, user_name: str, password: str):
        pass

    @abstractmethod
    def approve_reimbursement_by_id(self, reimbursement_id: int):
        pass

    @abstractmethod
    def deny_reimbursement_by_id(self, reimbursement_id: int, comment: str):
        pass

    @abstractmethod
    def view_pending_requests(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def view_past_requests(self) -> List[Reimbursement]:
        pass

    # stats
    @abstractmethod
    def view_total_amount_approved(self) -> List[TotalAmountApproved]:
        pass

    @abstractmethod
    def view_total_number_approved_requests(self) -> List[TotalNumberApprovedRequests]:
        pass

    @abstractmethod
    def view_total_number_denied_requests(self) -> List[TotalNumberDeniedRequests]:
        pass

    @abstractmethod
    def view_total_number_approved_food_drink(self) -> List[TotalNumberApprovedFoodDrink]:
        pass

    @abstractmethod
    def view_total_number_approved_transportation(self) -> List[TotalNumberApprovedTransportation]:
        pass

