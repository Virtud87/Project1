from abc import ABC, abstractmethod
from typing import List, Tuple

from entities.credentials import Credentials
from entities.reimbursement import Reimbursement
from entities.total_amount_approved import TotalAmountApproved
from entities.total_number_approved_food_drink import TotalNumberApprovedFoodDrink
from entities.total_number_approved_requests import TotalNumberApprovedRequests
from entities.total_number_approved_transportation import TotalNumberApprovedTransportation
from entities.total_number_denied_requests import TotalNumberDeniedRequests


class ManagerService(ABC):
    @abstractmethod
    def service_manager_login(self, credentials: Credentials):
        pass

    @abstractmethod
    def service_approve_reimbursement_by_id(self, reimbursement_id: int):
        pass

    @abstractmethod
    def service_deny_reimbursement_by_id(self, reimbursement_id: int, comment: str):
        pass

    @abstractmethod
    def service_view_pending_requests(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def service_view_past_requests(self) -> List[Reimbursement]:
        pass

    @abstractmethod
    def service_view_total_amount_approved(self) -> List[TotalAmountApproved]:
        pass

    @abstractmethod
    def service_view_total_number_approved_requests(self) -> List[TotalNumberApprovedRequests]:
        pass

    @abstractmethod
    def service_view_total_number_denied_requests(self) -> List[TotalNumberDeniedRequests]:
        pass

    @abstractmethod
    def service_view_total_number_approved_food_drink(self) -> List[TotalNumberApprovedFoodDrink]:
        pass

    @abstractmethod
    def service_view_total_number_approved_transportation(self) -> List[TotalNumberApprovedTransportation]:
        pass
