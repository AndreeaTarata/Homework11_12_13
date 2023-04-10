from behave import given, then, when

from pages.login_page import LoginPage


@given(u'I have a valid login url')
def step_impl(context):
    print(u'STEP: Given I have a valid login url')
    page = LoginPage(context.driver)
    assert page.open()


@given(u'I enter "{user}"')
def step_impl(context, user):
    print(u'STEP: Given I enter "{user}"')
    page = LoginPage(context.driver)
    page.enter_user(user)


@given(u'I enter password "{password}"')
def step_impl(context, password):
    print(u'STEP: Given I enter password"{password}"')
    page = LoginPage(context.driver)
    page.enter_password(password)


@when(u'I click on login button')
def step_impl(context):
    print(u'STEP: When I click on login button')
    page = LoginPage(context.driver)
    page.submit()


@then(u'the new URL will be "{keyword}"')
def step_impl(context, keyword):
    print(u'STEP: Then the new URL will be "https://the-internet.herokuapp.com/secure"')
    assert keyword in context.driver.url


@given(u'I have link on the login page')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given I have link on the login page')


@given(u'a href in elements')
def step_impl(context):
    raise NotImplementedError(u'STEP: Given a href in elements')


@when(u'I compare')
def step_impl(context):
    raise NotImplementedError(u'STEP: When I compare')


@then(u'the link \'Elemental Selenium\' is equal with the href')
def step_impl(context):
    raise NotImplementedError(u'STEP: Then the link \'Elemental Selenium\' is equal with the href')
