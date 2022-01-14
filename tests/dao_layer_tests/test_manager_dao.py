from dao_layer.implemented_classes.manager_postgres_dao import ManagerPostgresDAO

manager_postgres_dao = ManagerPostgresDAO()


def test_manager_login_success():
    login = manager_postgres_dao.manager_login("laPatrona", "bella1")
    assert login == (1,)


def test_approve_reimbursement_by_id_success():
    approved = manager_postgres_dao.approve_reimbursement_by_id(14)
    assert bool(approved)


def test_deny_reimbursement_by_id_success():
    denied = manager_postgres_dao.deny_reimbursement_by_id(2, "Over 40$ allowance.")
    assert bool(denied)


def test_view_pending_requests_success():
    pending_requests = manager_postgres_dao.view_pending_requests()
    assert len(pending_requests) >= 1


def test_view_past_requests_success():
    past_requests = manager_postgres_dao.view_past_requests()
    assert len(past_requests) >= 1


def test_view_total_amount_approved_by_employee_success():
    stats = manager_postgres_dao.view_total_amount_approved()
    assert len(stats) >= 1


def test_view_total_number_approved_requests_success():
    stats = manager_postgres_dao.view_total_number_approved_requests()
    assert len(stats) >= 1


def test_view_total_number_denied_requests_success():
    stats = manager_postgres_dao.view_total_number_denied_requests()
    assert len(stats) >= 1


def test_view_total_number_approved_food_drink_success():
    stats = manager_postgres_dao.view_total_number_approved_food_drink()
    assert len(stats) >= 1


def test_view_total_number_approved_transportation_success():
    stats = manager_postgres_dao.view_total_number_approved_transportation()
    assert bool(stats)
