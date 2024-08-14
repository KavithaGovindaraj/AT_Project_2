import unittest
from selenium import webdriver
from pages.login_page import LoginPage

class TestForgotPassword(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.maximize_window()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")

    def test_forgot_password(self):
        login_page = LoginPage(self.driver)
        login_page.click_forgot_password()
        login_page.enter_username("Admin")
        login_page.click_reset_password()
        login_page.print_reset_confirmation_message()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()
