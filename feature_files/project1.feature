Feature: Users should be able to manage their reimbursements

  Scenario: As an employee I can log in to view my console page
    Given The employee is on the home page
    When The employee enters their username
    When The employee enters their password
    When The employee clicks on login button
    Then The employee should be redirected to the employee home page

  Scenario: As an employee I should be able to submit new reimbursement requests so that I can get money back
    Given The employee is on the employee home page
    When The employee enters their reimbursement ID
    When The employee enters their employee ID
    When The employee enters the date
    When The employee enters the amount
    When The employee enters the reason
    Then The employee clicks on the submit button

  Scenario: As an employee I should be able to view my requests so that I know if they are approved or not
    Given The employee is on the employee home page
    Then The employee clicks on the view button

  Scenario: As an employee I should be able to log out so that my information is kept private
    Given The employee is on the employee home page
    When The employee clicks on the logout button
    Then The employee is redirected to the home page

  Scenario: As a manager I can log in to view my console page
    Given The manager is on the home page
    When The manager enters their username
    When The manager enters their password
    When The manager clicks on the login button
    Then The manager should be redirected to the manager home page

  Scenario: As a manager I should be able to view employees' pending requests
    Given The manager is on the manager home page
    Then The manager clicks on the view pending button

  Scenario: As a manager I should be able to approve reimbursement requests
    Given The manager is on the manager home page
    When The manager clicks on the view pending button
    Then The manager clicks on the approve button

  Scenario: As a manager I should be able to deny reimbursement requests with a comment
    Given The manager is on the manager home page
    When The manager clicks on the view pending button
    When The manager enters a comment
    Then The manager clicks on the deny button


  Scenario: As a manager I should be able to view employees' past requests
    Given The manager is on the manager home page
    Then The manager clicks on the view past button


  Scenario: As a manager I should be able to view reimbursement statistics
    Given The manager is on the manager home page
    When The manager clicks on the total amount approved per employee button
    When The manager clicks on the total requests approved per employee button
    When The manager clicks on the total requests denied per employee button
    When The manager clicks on the total food/drink requests approved per employee
    Then The manager clicks on the total transportation requests approved per employee

  Scenario: As a manager I should be able to log out to keep my information secure
    Given The manager is on the manager home page
    When The manager clicks on the logout button
    Then The manager is redirected to the home page