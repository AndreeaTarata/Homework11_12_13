import time

from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage


class LoginPage(BasePage):

    def open(self):
        self.driver.get(self.URL)
        time.sleep(5)

    def enter_user(self, value):
        self.driver.find_element(*LoginPageLocators.USER).send_keys(value)

    def enter_password(self, value):
        self.driver.find_element(*LoginPageLocators.PASSWORD).send_keys(value)

    def submit(self):
        self.driver.find_element(*LoginPageLocators.LOGINBTN).click()

    def new_URL(self):
        self.driver.find_element()




    def test2_page_title(self):
        expected = "The Internet"
        actual = self.driver.title
        self.assertEqual(expected, actual)

    def test3_verifica_Xpath(self):
        element = self.driver.find_element(*self.textul).text
        expected_text = "Login Page"
        self.assertEqual(element, expected_text)

    def test4_verifica_btn_Login(self):
        afisat = self.driver.find_element(*self.loginbtn).is_displayed()
        if afisat is True:
            print("Login button is displayed")
        else:
            print("Login button is not displayed")

    def test5_href(self):
        linkul = self.driver.find_element(By.LINK_TEXT, 'Elemental Selenium')
        actual_href = linkul.get_attribute('href')
        expected = 'http://elementalselenium.com/'
        self.assertEqual(actual_href, expected)

    def test6_empty_login(self):
        self.driver.find_element(*self.user).send_keys('')
        self.driver.find_element(*self.password).send_keys('')
        self.driver.find_element(*self.loginbtn).click()
        self.driver.find_element(*self.meseroare).is_displayed()

    def test7_invalid_login(self):
        self.driver.find_element(*self.user).send_keys('1')
        self.driver.find_element(*self.password).send_keys('2')
        self.driver.find_element(*self.loginbtn).click()
        actmes = self.driver.find_element(*self.meseroare).text
        expectedmes = 'Your username is invalid!'
        self.assertTrue(expectedmes in actmes, 'Error message text is incorrect')

    def test8_x_login(self):
        self.driver.find_element(*self.user).send_keys('')
        self.driver.find_element(*self.password).send_keys('')
        self.driver.find_element(*self.loginbtn).click()
        self.driver.find_element(*self.meseroare).is_displayed()
        self.driver.find_element(*self.xbtn).click()
        time.sleep(6)

    def test9_label(self):
        labels = self.driver.find_elements(By.TAG_NAME, 'label')
        lista = []
        for label in labels:
            lista.append(label.text)
        self.assertEqual(lista[0], 'Username')
        self.assertEqual(lista[1], 'Password')
        print(lista)
        time.sleep(7)

    def test10_secure(self):

        self.driver.find_element(*self.user).send_keys('tomsmith')
        self.driver.find_element(*self.password).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.loginbtn).click()
        # noul_url = self.driver.current_url
        # self.assertIn('/secure', noul_url)
        # wait = WebDriverWait(self.driver, 10)
        # success_message = wait.until(EC.visibility_of_element_located((By.CLASS_NAME, "flash.success"))) # de ce nu merge fara punct?
        # self.assertTrue(success_message.is_displayed())
        success_message = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "flash.success"))
        )
        self.assertTrue(success_message.is_displayed())

    def test11_logout(self):
        self.driver.find_element(*self.user).send_keys('tomsmith')
        self.driver.find_element(*self.password).send_keys('SuperSecretPassword!')
        self.driver.find_element(*self.loginbtn).click()
        self.driver.find_element(*self.loginbtn).click()
        logout_url = self.driver.current_url
        expected_logout_url = 'https://the-internet.herokuapp.com/login'
        self.assertTrue(logout_url, expected_logout_url)
