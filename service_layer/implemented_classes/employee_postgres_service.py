from typing import List

from custom_exceptions.custom_exceptions import NegativeDollarAmount, NonNumericAmount, UsernameOrPasswordIncorrect
from dao_layer.implemented_classes.employee_postgres_dao import EmployeePostgresDAO
from entities.reimbursement import Reimbursement
from service_layer.abstract_classes.employee_service import EmployeeService


class EmployeePostgresService(EmployeeService):
    def __init__(self, employee_dao: EmployeePostgresDAO):
        self.employee_dao = employee_dao

    def service_employee_login(self, user_name: str, password: str):
        employees = self.employee_dao.get_all_employees()
        for employee in employees:
            if employee.user_name == user_name and employee.password == password:
                return self.employee_dao.employee_login(user_name, password)
        raise UsernameOrPasswordIncorrect("Either your username or password or both are incorrect!")

    def service_submit_new_request(self, employee_id, date, amount, reason):
        check_float = isinstance(amount, float)
        if not check_float:
            raise NonNumericAmount("You must enter valid dollar amounts!")
        if amount < 0:
            raise NegativeDollarAmount("You cannot submit a negative dollar amount!")
        return self.employee_dao.submit_new_request(employee_id, date, amount, reason)

    def service_view_reimbursements_by_employee_id(self, validated) -> List[Reimbursement]:
        return self.employee_dao.view_reimbursements_by_employee_id(validated)
