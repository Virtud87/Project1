from dao_layer.implemented_classes.employee_postgres_dao import EmployeePostgresDAO
from entities.credentials import Credentials
from entities.submission import Submission

employee_dao_postgres = EmployeePostgresDAO()

new_submission = Submission(0, 1, "2021-12-09", 300.00, "food/drink")

credentials = Credentials("texasDan", "veritas1")


def test_login_success():
    login = employee_dao_postgres.login(credentials)
    assert bool(login)


def test_submit_new_request_success():
    request = employee_dao_postgres.submit_new_request(new_submission)
    assert bool(request)


def test_view_reimbursements_by_employee_id():
    view = employee_dao_postgres.view_reimbursements_by_employee_id(1)
    assert len(view) >= 1


def test_logout_success():
    logout = employee_dao_postgres.logout()
    assert bool(logout)
