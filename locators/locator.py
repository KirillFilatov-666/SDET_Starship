from selenium.webdriver.common.by import By

class FormLocators:
    INPUT_NAME = (By.ID, "name-input")
    INPUT_PASSWORD = (By.XPATH, "//input[@type='password']")
    MILK = (By.XPATH, "//label[@for='drink2' and text() = 'Milk']")
    COFFEE = (By.XPATH, "//label[@for='drink3' and text() = 'Coffee']")
    YELLOW = (By.XPATH, "//label[text()='Yellow']")
    SELECT_AUTOMATION = (By.XPATH, "//select[@name='automation']")
    OPTION_YES = (By.XPATH, "//option[@value='yes']")
    INPUT_EMAIL = (By.XPATH, "(//input[@type='text'])[2]")
    MESSAGE_FIELD = (By.XPATH, "//textarea[@name='message']")
    SUBMIT_BUTTON = (By.XPATH, "//button[@data-testid='submit-btn']")
    AUTOMATION_TOOLS_LIST = (By.XPATH, "//ul/li")
