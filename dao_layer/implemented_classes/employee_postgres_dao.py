from typing import List
from dao_layer.abstract_classes.employee_dao import EmployeeDAO
from entities.credentials import Credentials
from entities.employee import Employee
from entities.reimbursement import Reimbursement
from util.database_connection import connection


class EmployeePostgresDAO(EmployeeDAO):
    def get_all_employees(self):
        sql = "select * from employees"
        cursor = connection.cursor()
        cursor.execute(sql)
        employees = cursor.fetchall()
        employees_list = []
        for employee in employees:
            employees_list.append(Employee(*employee))
        return employees_list

    def employee_login(self, user_name: str, password: str):
        sql = "select employee_id from employees where user_name = %s and password = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (user_name, password))
        employee_id = cursor.fetchone()[0]
        return employee_id

    def return_employee_id(self, credentials: Credentials):
        sql = "select employee_id from employees where user_name = %s and password = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (credentials.user_name, credentials.password))
        employee_id = cursor.fetchone()
        return str(employee_id)

    def submit_new_request(self, employee_id, date, amount, reason):
        sql = "insert into reimbursements values(default, %s, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, (employee_id, date, amount, reason))
        connection.commit()
        return "success"

    def view_reimbursements_by_employee_id(self, validated) -> List[Reimbursement]:
        sql = "select * from reimbursements where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [validated])
        all_reimbursements = cursor.fetchall()
        reimbursements = []
        for reimbursement in all_reimbursements:
            reimbursements.append(Reimbursement(*reimbursement))
        return reimbursements
