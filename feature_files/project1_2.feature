Feature: The system should be able to handle errors

  Scenario: As the system I should reject failed login attempts
    Given The employee is on the home page
    When The employee enters their username
    When The employee enters the wrong password
    When The employee clicks on login button
    Then The system should reject the login attempt

  Scenario: As the system I should reject negative values for request amount
    Given The employee is on the employee home page
    When The employee enters their reimbursement ID
    When The employee enters their employee ID
    When The employee enters the date
    When The employee enters a negative value in amount
    When The employee enters the reason
    When The employee clicks on the submit button
    Then The system should reject the negative value

  Scenario: As the system I should reject non-numeric values for request amount
    Given The employee is on the employee home page
    When The employee enters their reimbursement ID
    When The employee enters their employee ID
    When The employee enters the date
    When The employee enters a non-numeric value in amount
    When The employee enters the reason
    When The employee clicks on the submit button
    Then The system should reject the non-numeric value