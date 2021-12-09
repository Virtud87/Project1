from typing import List

from dao_layer.abstract_classes.manager_dao import ManagerDAO
from util.database_connection import connection
from entities.reimbursement import Reimbursement


class ManagerPostgresDAO(ManagerDAO):
    def login(self, user_name: str, password: str) -> bool:
        pass

    def approve_reimbursement_by_id(self, reimbursement_id: int) -> bool:
        pass

    def deny_reimbursement_by_id(self, reimbursement_id: int) -> bool:
        pass

    def decision_comment_by_id(self, reimbursement: Reimbursement) -> bool:
        pass

    def view_pending_requests(self) -> List[Reimbursement]:
        pass

    def view_past_requests(self) -> List[Reimbursement]:
        pass

    def view_stats(self) -> List:
        pass

    def logout(self) -> bool:
        pass
