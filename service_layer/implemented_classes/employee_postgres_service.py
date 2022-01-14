from typing import List

from custom_exceptions.custom_exceptions import UsernameOrPasswordIncorrect, NegativeDollarAmount, NonNumericAmount
from dao_layer.implemented_classes.employee_postgres_dao import EmployeePostgresDAO
from entities.credentials import Credentials
from entities.reimbursement import Reimbursement
from entities.submission import Submission
from service_layer.abstract_classes.employee_service import EmployeeService

test_credentials = Credentials("texasDan", "veritas1")


class EmployeePostgresService(EmployeeService):
    def __init__(self, employee_dao: EmployeePostgresDAO):
        self.employee_dao = employee_dao

    def service_employee_login(self, user_name: str, password: str):
        validation = self.employee_dao.employee_login(user_name, password)
        if type(validation) == tuple:
            return True
        else:
            return False

    def service_submit_new_request(self, submission: Submission):
        check_float = isinstance(submission.amount, float)
        if not check_float:
            raise NonNumericAmount("You must enter valid dollar amounts!")
        if submission.amount < 0:
            raise NegativeDollarAmount("You cannot submit a negative dollar amount!")
        return self.employee_dao.submit_new_request(submission)

    def service_view_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        return self.employee_dao.view_reimbursements_by_employee_id(employee_id)
