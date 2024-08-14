from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions

class AdminPage:
    def __init__(self, driver):
        self.driver = driver
        self.driver.maximize_window()  # Maximize the window to prevent any visibility issues

        self.headers = {
            'User Management': (By.XPATH, "//header//span[h6[1]]"),
            'Job': (By.XPATH, "//header//span[h6[2]]"),
            'Organization': (By.XPATH, "//header//nav//li[3]//span"),
            'Qualifications': (By.XPATH, "//header//nav//li[4]//span"),
            'Nationalities': (By.XPATH, "//header//nav//li[5]//a"),
            'Corporate Banking': (By.XPATH, "//header//nav//li[6]//a"),
            'Configuration': (By.XPATH, "//header//nav//li[6]//a")
           }
        self.url = "https://opensource-demo.orangehrmlive.com/web/index.php/admin/viewSystemUsers"
        self.page_title = "OrangeHRM"

        self.main_menu = {
            "Admin": (By.XPATH, "//a[contains(@href, '/admin')]"),
            "PIM": (By.XPATH, "//a[contains(@href, '/pim')]"),
            "Leave": (By.XPATH, "//a[contains(@href, '/leave')]"),
            "Time": (By.XPATH, "//a[contains(@href, '/time')]"),
            "Recruitment": (By.XPATH, "//a[contains(@href, '/recruitment')]"),
            "My Info": (By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a/span"),
            "Performance": (By.XPATH, "//a[contains(@href, '/performance')]"),
            "Dashboard": (By.XPATH, "//a[contains(@href, '/dashboard')]"),
            "Directory": (By.XPATH, "//a[contains(@href, '/directory')]"),
            "Maintenance": (By.XPATH, "//a[contains(@href, '/maintenance')]"),
            "Buzz": (By.XPATH, "//a[contains(@href, '/buzz')]")
        }

    def navigate_to_admin_page(self):
        try:
            self.driver.get(self.url)
            WebDriverWait(self.driver, 10).until(
                expected_conditions.title_contains(self.page_title)
            )
            print("Navigation to Admin page successful.")
        except Exception as e:
            print(f"Navigation Error: {e}")
            self.driver.save_screenshot("navigation_error.png")
            raise

    def validate_page_title(self):
        try:
            WebDriverWait(self.driver, 10).until(
                expected_conditions.title_contains(self.page_title)
            )
            print("Page title validation successful.")

        except Exception as e:
            print(f"Page Title Error: {e}")
            self.driver.save_screenshot("page_title_error.png")
            raise

    def validate_header_options(self):
        for header, locator in self.headers.items():
            try:
                element = WebDriverWait(self.driver, 40).until(
                    expected_conditions.presence_of_element_located(locator)
                )
                # Scroll the element into view if necessary
                self.driver.execute_script("arguments[0].scrollIntoView();", element)
                print(f"Header '{header}' is present.")
            except Exception as e:
                print(f"Header '{header}' is not present. Error: {e}")
                self.driver.save_screenshot(f"header_validation_error_{header}.png")
        print("Admin page header validation completed.")

    def validate_main_menu(self):
        # Validate that each main menu item is present and visible
        for name, locator in self.main_menu.items():
            try:
                WebDriverWait(self.driver, 20).until(
                    expected_conditions.visibility_of_element_located(locator)
                )
                print(f"Main menu '{name}' is present and visible.")

            except Exception as e:
                print(f"Main menu '{name}' is not present or visible. Error: {e}")
                # Optionally take a screenshot
                self.driver.save_screenshot(f"main_menu_validation_error_{name}.png")
        print("Admin page main menu validation completed.")
