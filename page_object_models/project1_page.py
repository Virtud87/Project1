from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


class Project1HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_employee_username(self):
        element: WebDriver = self.driver.find_element(By.ID, "employee-username")
        return element

    def enter_employee_password(self):
        element: WebDriver = self.driver.find_element(By.ID, "employee-password")
        return element

    def click_employee_login(self):
        element: WebDriver = self.driver.find_element(By.ID, "employee-login")
        return element

    def enter_manager_username(self):
        element: WebDriver = self.driver.find_element(By.ID, "manager-username")
        return element

    def enter_manager_password(self):
        element: WebDriver = self.driver.find_element(By.ID, "manager-password")
        return element

    def click_manager_login(self):
        element: WebDriver = self.driver.find_element(By.ID, "manager-login")
        return element


class EmployeeHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def enter_reimbursement_id(self):
        element: WebDriver = self.driver.find_element(By.ID, "reimbursementId")
        return element

    def enter_employee_id(self):
        element: WebDriver = self.driver.find_element(By.ID, "employeeId")
        return element

    def enter_date(self):
        element: WebDriver = self.driver.find_element(By.ID, "date")
        return element

    def enter_amount(self):
        element: WebDriver = self.driver.find_element(By.ID, "amount")
        return element

    def enter_reason(self):
        element: WebDriver = self.driver.find_element(By.ID, "reason")
        return element

    def click_employee_submit(self):
        element: WebDriver = self.driver.find_element(By.ID, "employee-submit")
        return element

    def click_view_button(self):
        element: WebDriver = self.driver.find_element(By.ID, "viewRequests")
        return element

    def employee_logout(self):
        element: WebDriver = self.driver.find_element(By.ID, "employeeLogout")
        return element


class ManagerHomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def click_view_button(self):
        element: WebDriver = self.driver.find_element(By.ID, "managerView")
        return element

    def click_approve_button(self):
        element: WebDriver = self.driver.find_element(By.XPATH, '//*[@id="table-body-pending"]/tr[1]/td[8]/button')
        return element

    def click_comment_section(self):
        element: WebDriver = self.driver.find_element(By.XPATH, '//*[@id="table-body-pending"]/tr[2]/td[10]/input')
        return element

    def click_deny_button(self):
        element: WebDriver = self.driver.find_element(By.XPATH, '//*[@id="table-body-pending"]/tr[2]/td[9]/button')
        return element

    def click_past_button(self):
        element: WebDriver = self.driver.find_element(By.ID, "managerPastButton")
        return element

    def click_total_amount_approved_button(self):
        element: WebDriver = self.driver.find_element(By.ID, "amountApproved")
        return element

    def click_total_requests_approved_button(self):
        element: WebDriver = self.driver.find_element(By.ID, "requestsApproved")
        return element

    def click_total_requests_denied_button(self):
        element: WebDriver = self.driver.find_element(By.ID, "requestsDenied")
        return element

    def click_total_food_drink_button(self):
        element: WebDriver = self.driver.find_element(By.ID, "foodDrink")
        return element

    def click_total_transportation_button(self):
        element: WebDriver = self.driver.find_element(By.ID, "transportation")
        return element

    def click_manager_logout(self):
        element: WebDriver = self.driver.find_element(By.ID, "managerLogout")
        return element
