from custom_exceptions.custom_exceptions import UsernameOrPasswordIncorrect, NegativeDollarAmount, NonNumericAmount
from dao_layer.implemented_classes.employee_postgres_dao import EmployeePostgresDAO
from entities.credentials import Credentials
from entities.submission import Submission
from service_layer.implemented_classes.employee_postgres_service import EmployeePostgresService

employee_dao = EmployeePostgresDAO()

employee_service = EmployeePostgresService(employee_dao)

submission = Submission(0, 1, "2021-12-09", "string", "transportation")

credentials = Credentials("User", "pwd")


def test_service_login():
    try:
        employee_service.service_login(credentials)
        assert False
    except UsernameOrPasswordIncorrect as e:
        assert str(e) == "Either your user name or password or both are incorrect!"


def test_service_submit_new_request():
    try:
        employee_service.service_submit_new_request(submission)
        assert False
    except NegativeDollarAmount as e:
        assert str(e) == "You cannot submit a negative dollar amount!"
    except NonNumericAmount as e:
        assert str(e) == "You must enter valid dollar amounts!"
