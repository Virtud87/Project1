from dao_layer.implemented_classes.manager_postgres_dao import ManagerPostgresDAO
from entities.reimbursement import Reimbursement

manager_dao_postgres = ManagerPostgresDAO()

reimbursement_comment = Reimbursement(1, "2021-12-09", 25.00, "food", "denied", "Went over allowance of $20.00")


def test_login_success():
    login = manager_dao_postgres.login("laPatrona", "bella1")
    assert bool(login)


def test_approve_reimbursement_by_id_success():
    approved = manager_dao_postgres.approve_reimbursement_by_id(1)
    assert bool(approved)


def test_deny_reimbursement_by_id_success():
    denied = manager_dao_postgres.deny_reimbursement_by_id(2)
    assert bool(denied)


def test_decision_comment_by_id_success():
    comment = manager_dao_postgres.decision_comment_by_id(reimbursement_comment)
    assert bool(comment)


def test_view_pending_requests_success():
    pending_requests = manager_dao_postgres.view_pending_requests()
    assert len(pending_requests) >= 1


def test_view_past_requests_success():
    past_requests = manager_dao_postgres.view_past_requests()
    assert len(past_requests) >= 1


def test_view_stats_success():
    stats = manager_dao_postgres.view_stats()
    assert len(stats) >= 1


def test_logout_success():
    logged_out = manager_dao_postgres.logout()
    assert bool(logged_out)
