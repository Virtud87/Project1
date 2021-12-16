from typing import List, Tuple

from custom_exceptions.custom_exceptions import UsernameOrPasswordIncorrect
from dao_layer.implemented_classes.manager_postgres_dao import ManagerPostgresDAO
from entities.credentials import Credentials
from entities.reimbursement import Reimbursement
from entities.total_amount_approved import TotalAmountApproved
from entities.total_number_approved_food_drink import TotalNumberApprovedFoodDrink
from entities.total_number_approved_requests import TotalNumberApprovedRequests
from entities.total_number_approved_transportation import TotalNumberApprovedTransportation
from entities.total_number_denied_requests import TotalNumberDeniedRequests
from service_layer.abstract_classes.manager_service import ManagerService

test_credentials = Credentials("laPatrona", "bella1")


class ManagerPostgresService(ManagerService):
    def __init__(self, manager_dao: ManagerPostgresDAO):
        self.manager_dao = manager_dao

    def service_manager_login(self, credentials: Credentials):
        credentials_returned = self.manager_dao.manager_login(credentials)
        if credentials_returned is None:
            raise UsernameOrPasswordIncorrect("Either your user name or password or both are incorrect!")
        return self.manager_dao.return_manager_id(credentials)

    def service_approve_reimbursement_by_id(self, reimbursement_id: int):
        return self.manager_dao.approve_reimbursement_by_id(reimbursement_id)

    def service_deny_reimbursement_by_id(self, reimbursement_id: int, comment: str):
        return self.manager_dao.deny_reimbursement_by_id(reimbursement_id, comment)

    def service_view_pending_requests(self) -> List[Reimbursement]:
        return self.manager_dao.view_pending_requests()

    def service_view_past_requests(self) -> List[Reimbursement]:
        return self.manager_dao.view_past_requests()

    def service_view_total_amount_approved(self) -> List[TotalAmountApproved]:
        return self.manager_dao.view_total_amount_approved()

    def service_view_total_number_approved_requests(self) -> List[TotalNumberApprovedRequests]:
        return self.manager_dao.view_total_number_approved_requests()

    def service_view_total_number_denied_requests(self) -> List[TotalNumberDeniedRequests]:
        return self.manager_dao.view_total_number_denied_requests()

    def service_view_total_number_approved_food_drink(self) -> List[TotalNumberApprovedFoodDrink]:
        return self.manager_dao.view_total_number_approved_food_drink()

    def service_view_total_number_approved_transportation(self) -> List[TotalNumberApprovedTransportation]:
        return self.manager_dao.view_total_number_approved_transportation()
