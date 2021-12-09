from dao_layer.implemented_classes.employee_postgres_dao import EmployeePostgresDAO

employee_dao_postgres = EmployeePostgresDAO()


def test_login_success():
    login = employee_dao_postgres.login("texasDan", "veritas1")
    assert bool(login)


def test_submit_new_request_success():
    request = employee_dao_postgres.submit_new_request('2021-12-09', 15.00, "food/drink")
    assert bool(request)


def test_view_requests_by_employee_id():
    view = employee_dao_postgres.view_requests_by_employee_id(1)
    assert len(view) >= 1


def test_logout_success():
    logout = employee_dao_postgres.logout()
    assert bool(logout)
