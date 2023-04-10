from selenium.webdriver.common.by import By


class LogoutPageLocators:
    MESEROARE = (By.ID, 'flash-messages')
    XBTN = (By.CLASS_NAME, 'close')
    LABEL_USERNAME = (By.XPATH, '//*[@id="login"]/div[1]/div/label')
    LABEL_PSD = (By.XPATH, '//*[@id="login"]/div[2]/div/label')
    LOGOUTBTN = (By.CLASS_NAME, 'icon-2x icon-signout')
    TEXT = (By.CLASS_NAME, 'subheader')
    TEXT_SECURE_AREA = (By.TAG_NAME, 'h2')
    SUCCES_LOGIN_URL = "https://the-internet.herokuapp.com/secure"