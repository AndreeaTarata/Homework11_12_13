Feature: Details from page 'https://the-internet.herokuapp.com/'
  As a user
  I want to navigate to all links from url "https://the-internet.herokuapp.com/login"
  So I can acknowledge all info

  Scenario: test href from 'Elemental Selenium' link
    Given I have link on the login page
    And a href in elements
    When I compare
    Then the link 'Elemental Selenium' is equal with the href