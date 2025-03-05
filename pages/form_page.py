from config import URL
from pages.base_page import BasePage
from locators.locator import FormLocators


class FormPage(BasePage):

    def open(self):
        super().open(URL)

    def fill_name(self, name):
        self.fill_input(FormLocators.INPUT_NAME, name)

    def fill_password(self, password):
        self.fill_input(FormLocators.INPUT_PASSWORD, password)

    def select_drinks(self):
        self.click_element(FormLocators.MILK)
        self.click_element(FormLocators.COFFEE)

    def select_color(self):
        self.click_element(FormLocators.YELLOW)

    def select_automation(self):
        self.select_dropdown_by_text(FormLocators.SELECT_AUTOMATION, "Yes")

    def fill_email(self, email):
        self.fill_input(FormLocators.INPUT_EMAIL, email)

    def fill_message(self):
        self.wait_for_element(FormLocators.AUTOMATION_TOOLS_LIST)
        tools = self.driver.find_elements(*FormLocators.AUTOMATION_TOOLS_LIST)

        num_tools = len(tools)
        longest_tool = max((tool.text for tool in tools), key=len) if tools else "Нет инструментов"

        message_text = f"Количество инструментов: {num_tools}. Самый длинный: {longest_tool}"
        self.fill_input(FormLocators.MESSAGE_FIELD, message_text)

    def submit_form(self):
        self.click_element(FormLocators.SUBMIT_BUTTON)

    def check_alert_message(self):
        return self.accept_alert()
