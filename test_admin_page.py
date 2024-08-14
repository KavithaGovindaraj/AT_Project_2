import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from pages.login_page import LoginPage
from pages.admin_page import AdminPage

class TestAdminPage(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Edge()
        self.driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
        login_page = LoginPage(self.driver)
        login_page.enter_username("Admin")
        login_page.enter_password("admin123")
        login_page.click_login()
        # Wait for URL to contain a specific string or verify navigation
        WebDriverWait(self.driver, 20).until(lambda driver: "dashboard" in driver.current_url.lower())

    def test_admin_page_headers(self):
        admin_page = AdminPage(self.driver)
        admin_page.navigate_to_admin_page()
        admin_page.validate_page_title()
        admin_page.validate_header_options()

    def test_admin_page_main_menu(self):
        admin_page = AdminPage(self.driver)
        admin_page.navigate_to_admin_page()
        admin_page.validate_main_menu()

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    unittest.main()