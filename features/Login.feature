Feature: Login into the page 'https://the-internet.herokuapp.com/'
  As a user
  I want to login to "https://the-internet.herokuapp.com/login"
  So I can enter my account safely

  @functionality
  Scenario Outline: login successfully
    Given I have a valid login url
    And I enter "<user>"
    And I enter password "<password>"
    When I click on login button
    Then the new URL will be "https://the-internet.herokuapp.com/secure"
    Examples:
      | user | password |
      | tomsmith | SuperSecretPassword! |






