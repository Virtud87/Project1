from custom_exceptions.custom_exceptions import UsernameOrPasswordIncorrect
from dao_layer.implemented_classes.manager_postgres_dao import ManagerPostgresDAO
from service_layer.implemented_classes.manager_postgres_service import ManagerPostgresService

manager_dao = ManagerPostgresDAO()

manager_service = ManagerPostgresService(manager_dao)


def test_service_manager_login():
    try:
        if manager_service.service_manager_login("laa", "bella1"):
            assert False
    except UsernameOrPasswordIncorrect as e:
        assert str(e) == "Either your user name or password or both are incorrect!"
