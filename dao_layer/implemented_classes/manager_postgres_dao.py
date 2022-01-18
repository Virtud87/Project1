from typing import List
from dao_layer.abstract_classes.manager_dao import ManagerDAO
from entities.manager import Manager
from entities.total_amount_approved import TotalAmountApproved
from entities.total_number_approved_food_drink import TotalNumberApprovedFoodDrink
from entities.total_number_approved_requests import TotalNumberApprovedRequests
from entities.total_number_approved_transportation import TotalNumberApprovedTransportation
from entities.total_number_denied_requests import TotalNumberDeniedRequests
from util.database_connection import connection
from entities.reimbursement import Reimbursement


class ManagerPostgresDAO(ManagerDAO):
    def get_all_managers(self):
        sql = "select * from managers"
        cursor = connection.cursor()
        cursor.execute(sql)
        managers = cursor.fetchall()
        managers_list = []
        for manager in managers:
            managers_list.append(Manager(*manager))
        return managers_list

    def manager_login(self, user_name: str, password: str):
        sql = "select manager_id from managers where user_name = %s and password = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (user_name, password))
        manager_id = cursor.fetchone()[0]
        return manager_id

    def return_manager_id(self, user_name: str, password: str):
        sql = "select manager_id from managers where user_name = %s and password = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (user_name, password))
        manager_id = cursor.fetchone()
        return str(manager_id)

    def approve_reimbursement_by_id(self, reimbursement_id: int):
        sql = "update reimbursements set status = 'approved' where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [reimbursement_id])
        connection.commit()
        return str(reimbursement_id)

    def deny_reimbursement_by_id(self, reimbursement_id: int, comment: str):
        sql = "update reimbursements set status = 'denied', comment = %s where reimbursement_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (comment, reimbursement_id))
        connection.commit()
        return str(reimbursement_id)

    def view_pending_requests(self) -> List[Reimbursement]:
        sql = "select * from reimbursements where status = 'pending'"
        cursor = connection.cursor()
        cursor.execute(sql)
        pending = cursor.fetchall()
        pending_list = []
        for reimburse in pending:
            pending_list.append(Reimbursement(*reimburse))
        return pending_list

    def view_past_requests(self) -> List[Reimbursement]:
        sql = "select * from reimbursements where status = 'approved' or status = 'denied'"
        cursor = connection.cursor()
        cursor.execute(sql)
        past = cursor.fetchall()
        past_list = []
        for reimburse in past:
            past_list.append(Reimbursement(*reimburse))
        return past_list

    def view_total_amount_approved(self) -> List[TotalAmountApproved]:
        sql = "select * from total_amount_approved_per_employee"
        cursor = connection.cursor()
        cursor.execute(sql)
        returned = cursor.fetchall()
        list_returned = []
        for item in returned:
            list_returned.append(TotalAmountApproved(*item))
        return list_returned

    def view_total_number_approved_requests(self) -> List[TotalNumberApprovedRequests]:
        sql = "select * from total_requests_approved_per_employee"
        cursor = connection.cursor()
        cursor.execute(sql)
        returned = cursor.fetchall()
        list_returned = []
        for item in returned:
            list_returned.append(TotalNumberApprovedRequests(*item))
        return list_returned

    def view_total_number_denied_requests(self) -> List[TotalNumberDeniedRequests]:
        sql = "select * from total_requests_denied_per_employee"
        cursor = connection.cursor()
        cursor.execute(sql)
        returned = cursor.fetchall()
        list_returned = []
        for item in returned:
            list_returned.append(TotalNumberDeniedRequests(*item))
        return list_returned

    def view_total_number_approved_food_drink(self) -> List[TotalNumberApprovedFoodDrink]:
        sql = "select * from total_food_drink_requests_per_employee"
        cursor = connection.cursor()
        cursor.execute(sql)
        returned = cursor.fetchall()
        list_returned = []
        for item in returned:
            list_returned.append(TotalNumberApprovedFoodDrink(*item))
        return list_returned

    def view_total_number_approved_transportation(self) -> List[TotalNumberApprovedTransportation]:
        sql = "select * from total_transportation_requests_per_employee"
        cursor = connection.cursor()
        cursor.execute(sql)
        returned = cursor.fetchall()
        list_returned = []
        for item in returned:
            list_returned.append(TotalNumberApprovedTransportation(*item))
        return list_returned
