from typing import List

from dao_layer.abstract_classes.employee_dao import EmployeeDAO
from entities.credentials import Credentials
from entities.reimbursement import Reimbursement
from entities.submission import Submission
from util.database_connection import connection


class EmployeePostgresDAO(EmployeeDAO):
    def employee_login(self, credentials: Credentials):
        sql = "select user_name, password from employees where user_name = %s and password = %s"
        cursor = connection.cursor()
        cursor.execute(sql, (credentials.user_name, credentials.password))
        connection.commit()
        credentials = cursor.fetchone()
        return credentials

    def submit_new_request(self, submission: Submission):
        sql = "insert into reimbursements values(default, %s, %s, %s, %s)"
        cursor = connection.cursor()
        cursor.execute(sql, (submission.employee_id, submission.date, submission.amount, submission.reason))
        connection.commit()
        return submission

    def view_reimbursements_by_employee_id(self, employee_id: int) -> List[Reimbursement]:
        sql = "select * from reimbursements where employee_id = %s"
        cursor = connection.cursor()
        cursor.execute(sql, [employee_id])
        all_reimbursements = cursor.fetchall()
        reimbursements = []
        for reimbursement in all_reimbursements:
            reimbursements.append(Reimbursement(*reimbursement))
        return reimbursements
