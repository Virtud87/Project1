from behave import Given, When, Then
import time

from behave.formatter import null


@Given(u'The employee is on the home page')
def get_project1_home(context):
    context.driver.get("http://127.0.0.1:5500/index.html")


@When(u'The employee enters their username')
def enter_employee_username(context):
    context.project1_home.enter_employee_username().send_keys("texasDan")


@When(u'The employee enters their password')
def enter_employee_password(context):
    context.project1_home.enter_employee_password().send_keys("veritas1")


@When(u'The employee clicks on login button')
def click_employee_login(context):
    context.project1_home.click_employee_login().click()


@Then(u'The employee should be redirected to the employee home page')
def redirect_to_employee_home_page(context):
    time.sleep(1)
    title = context.driver.title
    assert title == "Employee Home"


@Given(u'The employee is on the employee home page')
def employee_home(context):
    context.driver.get("http://127.0.0.1:5500/employee_home.html")


@When(u'The employee enters their reimbursement ID')
def enter_reimbursement_id(context):
    context.employee_home.enter_reimbursement_id().send_keys(1)


@When(u'The employee enters their employee ID')
def enter_employee_id(context):
    context.employee_home.enter_employee_id().send_keys(1)


@When(u'The employee enters the date')
def enter_date(context):
    context.employee_home.enter_date().send_keys("2021-12-20")


@When(u'The employee enters the amount')
def enter_amount(context):
    context.employee_home.enter_amount().send_keys(37.50)


@When(u'The employee enters the reason')
def enter_reason(context):
    context.employee_home.enter_reason().send_keys("transportation")


@Then(u'The employee clicks on the submit button')
def click_employee_submit(context):
    context.employee_home.click_employee_submit().click()


@When(u'The employee clicks on the submit button')
def click_employee_submit(context):
    context.employee_home.click_employee_submit().click()
    time.sleep(1)


@Then(u'The employee clicks on the view button')
def click_view_button(context):
    context.employee_home.click_view_button().click()


@When(u'The employee clicks on the logout button')
def employee_logout(context):
    context.employee_home.employee_logout().click()


@Then(u'The employee is redirected to the home page')
def employee_logout_redirect(context):
    assert context.driver.title == "Login Page"


# MANAGER
@Given(u'The manager is on the home page')
def project1_home(context):
    get_project1_home(context)


@When(u'The manager enters their username')
def enter_manager_username(context):
    context.project1_home.enter_manager_username().send_keys("laPatrona")


@When(u'The manager enters their password')
def enter_manager_password(context):
    context.project1_home.enter_manager_password().send_keys("bella1")


@When(u'The manager clicks on the login button')
def click_manager_login(context):
    context.project1_home.click_manager_login().click()


@Then(u'The manager should be redirected to the manager home page')
def redirect_to_manager_home_page(context):
    time.sleep(.5)
    title = context.driver.title
    assert title == "Manager Home"


@Given(u'The manager is on the manager home page')
def manager_home(context):
    context.driver.get("http://127.0.0.1:5500/manager_home.html")


@Then(u'The manager clicks on the view pending button')
def click_view_button(context):
    context.manager_home.click_view_button().click()
    time.sleep(1)


@When(u'The manager clicks on the view pending button')
def click_view_button(context):
    context.manager_home.click_view_button().click()
    time.sleep(1)


@Then(u'The manager clicks on the approve button')
def click_approve_button(context):
    context.manager_home.click_approve_button().click()


@When(u'The manager enters a comment')
def enter_comment(context):
    context.manager_home.click_comment_section().send_keys("Over 40$ allowance")


@Then(u'The manager clicks on the deny button')
def click_deny_button(context):
    context.manager_home.click_deny_button().click()


@Then(u'The manager clicks on the view past button')
def click_past_button(context):
    context.manager_home.click_past_button().click()


@When(u'The manager clicks on the total amount approved per employee button')
def click_total_amount_approved_button(context):
    context.manager_home.click_total_amount_approved_button().click()


@When(u'The manager clicks on the total requests approved per employee button')
def click_total_requests_approved_button(context):
    context.manager_home.click_total_requests_approved_button().click()


@When(u'The manager clicks on the total requests denied per employee button')
def click_total_requests_denied_button(context):
    context.manager_home.click_total_requests_denied_button().click()


@When(u'The manager clicks on the total food/drink requests approved per employee')
def click_total_food_drink_button(context):
    context.manager_home.click_total_food_drink_button().click()


@Then(u'The manager clicks on the total transportation requests approved per employee')
def click_total_transportation_button(context):
    context.manager_home.click_total_transportation_button().click()


@When(u'The manager clicks on the logout button')
def click_manager_logout(context):
    context.manager_home.click_manager_logout().click()


@Then(u'The manager is redirected to the home page')
def manager_logout_redirect(context):
    assert context.driver.title == "Login Page"


# Feature 2
@When(u'The employee enters the wrong password')
def enters_incorrect_password(context):
    context.project1_home.enter_employee_password().send_keys("veritas")


@Then(u'The system should reject the login attempt')
def reject_login_attempt(context):
    assert context.driver.switch_to.alert.text == "Either your username or password or both are incorrect!"
    context.driver.switch_to.alert.accept()


@When(u'The employee enters a negative value in amount')
def enters_negative_value(context):
    context.employee_home.enter_amount().send_keys(-20)


@Then(u'The system should reject the negative value')
def reject_negative(context):
    assert context.employee_home.enter_amount().text != null


@When(u'The employee enters a non-numeric value in amount')
def enters_non_numeric_value(context):
    context.employee_home.enter_amount().send_keys("value")


@Then(u'The system should reject the non-numeric value')
def reject_non_numeric(context):
    assert context.employee_home.enter_amount().text != null
