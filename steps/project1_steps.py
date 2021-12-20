from behave import Given, When, Then


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
def redirect_to_employee_home_page(context, title: str):
    assert context.driver.title == "Employee Home"


@Given(u'The employee is on the employee home page')
def employee_home(context):
    context.driver.get("http://127.0.0.1:5500/employee_home.html")


@When(u'The employee enters 1 into the reimbursement ID')
def enter_reimbursement_id(context):
    context.driver.enter_reimbursement_id().send_keys(1)


@When(u'The employee enters 1 into the employee ID')
def enter_employee_id(context):
    context.driver.enter_employee_id().send_keys(1)


@When(u'The employee enters 2021-12-19 into the date')
def enter_date(context):
    context.driver.enter_date().send_keys("2021-12-19")


@When(u'The employee enters 37.50 into the amount')
def enter_amount(context):
    context.driver.enter_amount().send_keys(37.50)


@When(u'The employee enters transportation the reason')
def enter_reason(context):
    context.driver.enter_reason().send_keys("transportation")


@Then(u'The employee clicks on the submit button')
def click_employee_submit(context):
    context.driver.click_employee_submit().click()


@Then(u'The employee clicks on the view button')
def click_view_button(context):
    context.driver.click_view_button().click()


# @Then(u'The requests are populated')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then The requests are populated')


@When(u'The employee clicks on the logout button')
def employee_logout(context):
    context.driver.employee_logout().click()


@Then(u'The employee is redirected to the home page')
def employee_logout_redirect(context):
    assert context.driver.title == "Login Page"


# MANAGER
@Given(u'The manager is on the home page')
def project1_home(context):
    get_project1_home(context)
    # context.driver.get("http://127.0.0.1:5500/index.html")


@When(u'The manager enters laPatrona into the username')
def enter_manager_username(context):
    context.driver.enter_manager_username().send_keys("laPatrona")


@When(u'The manager enters bella1 into the password')
def enter_manager_password(context):
    context.driver.enter_manager_password().send_keys("bella1")


@When(u'The manager clicks on the login button')
def click_manager_login(context):
    context.driver.click_manager_login().click()


@Then(u'The manger should be redirected to the manager home page')
def redirect_to_manager_home_page(context):
    assert context.driver.title == "Manager Home"


@Given(u'The manager is on the manager home page')
def manager_home(context):
    context.driver.get("http://127.0.0.1:5500/manager_home.html")


@When(u'The manger clicks on the view pending button')
def click_view_button(context):
    context.driver.click_view_button().click()


# @Then(u'The pending requests are populated')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then The pending requests are populated')


# @Given(u'The manager has clicked on the view pending button')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Given The manager has clicked on the view pending button')


@Then(u'The manager clicks on the approve button')
def click_approve_button(context):
    context.driver.click_approve_button().click()


# @Then(u'The request is removed from the pending list')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then The request is removed from the pending list')


@When(u'The manager enters Over 40$ allowance into the comment')
def enter_comment(context):
    context.driver.click_comment_section().send_keys("Over 40$ allowance")


@Then(u'The manager clicks on the deny button')
def click_deny_button(context):
    context.driver.click_deny_button().click()


@Then(u'The manager clicks on the view past button')
def click_past_button(context):
    context.driver.click_past_button().click()


# @Then(u'The past requests are populated')
# def step_impl(context):
#     raise NotImplementedError(u'STEP: Then The past requests are populated')


@When(u'The manager clicks on the total amount approved per employee button')
def click_total_amount_approved_button(context):
    context.driver.click_total_amount_approved_button().click()


@When(u'The manager clicks on the total requests approved per employee button')
def click_total_requests_approved_button(context):
    context.driver.click_total_requests_approved_button().click()


@When(u'The manager clicks on the total requests denied per employee button')
def click_total_requests_denied_button(context):
    context.driver.click_total_requests_denied_button().click()


@When(u'The manager clicks on the total food/drink requests approved per employee')
def click_total_food_drink_button(context):
    context.driver.click_total_food_drink_button().click()


@Then(u'The manager clicks on the total transportation requests approved per employee')
def click_total_transportation_button(context):
    context.driver.click_total_transportation_button().click()


@When(u'The manager clicks on the logout button')
def click_manager_logout(context):
    context.driver.click_manager_logout().click()


@Then(u'The manager is redirected to the home page')
def manager_logout_redirect(context):
    assert context.driver.title == "Login Page"
