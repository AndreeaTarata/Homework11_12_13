from selenium.webdriver.common.by import By


class LoginPageLocators:
    USER = (By.ID, 'username')
    PASSWORD = (By.ID, 'password')
    LOGINBTN = (By.CLASS_NAME, 'radius')
    TEXTUL = (By.XPATH, '//h2')

