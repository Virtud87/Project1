from behave.runner import Context
from selenium import webdriver
from page_object_models.project1_page import Project1HomePage, EmployeeHomePage, ManagerHomePage


def before_all(context: Context):
    context.driver = webdriver.Chrome("chromedriver.exe")
    context.project1_home = Project1HomePage(context.driver)
    context.project1_home = EmployeeHomePage(context.driver)
    context.project1_home = ManagerHomePage(context.driver)


def after_all(context):
    context.driver.quit()
