from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver

    USERNAME_TEXTBOX = (By.CSS_SELECTOR, "input[data-id='username']")
    PASSWORD_TEXTBOX = (By.CSS_SELECTOR, "input[data-id='password']")
    LOGIN_BUTTON = (By.CSS_SELECTOR, "button[type='submit']")

    def enter_username(self, username):
        self.driver.find_element(*LoginPage.USERNAME_TEXTBOX).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*LoginPage.PASSWORD_TEXTBOX).send_keys(password)

    def click_login(self):
        self.driver.find_element(*LoginPage.LOGIN_BUTTON).click()










