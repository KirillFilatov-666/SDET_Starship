import time

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)  # Явное ожидание (10 секунд)

    def open(self, url):
        self.driver.get(url)

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def click_element(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", element)
        time.sleep(1)
        self.wait.until(EC.element_to_be_clickable(locator)).click()

    def fill_input(self, locator, text):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def select_dropdown_by_text(self, locator, text):
        from selenium.webdriver.support.ui import Select
        dropdown = Select(self.wait.until(EC.presence_of_element_located(locator)))
        dropdown.select_by_visible_text(text)

    def wait_for_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    def scroll_to_element(self, locator):
        element = self.wait_for_element(locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)

    def press_enter(self, locator):
        element = self.wait.until(EC.presence_of_element_located(locator))
        element.send_keys(Keys.ENTER)

    def accept_alert(self):
        alert = self.wait.until(EC.alert_is_present())
        alert_text = alert.text
        alert.accept()
        return alert_text
