Feature: Login into the page 'https://the-internet.herokuapp.com/'
  As a user
  I want to logout from "https://the-internet.herokuapp.com/secure"
  So I can exit my account safely
  Scenario Outline: test logout url
    Given I have a valid user
    And a valid password
    When I click on login button
    And than on logout button
    Then the new url is 'https://the-internet.herokuapp.com/login'
    Examples:
      |  |