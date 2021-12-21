from behave.runner import Context
from selenium import webdriver
from page_object_models.project1_page import Project1HomePage, EmployeeHomePage, ManagerHomePage


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver")
    # context.driver.set_window_size(1920, 1080)
    context.project1_home = Project1HomePage(context.driver)
    context.employee_home = EmployeeHomePage(context.driver)
    context.manager_home = ManagerHomePage(context.driver)
    context.driver.implicitly_wait(1)


def after_all(context):
    context.driver.quit()
