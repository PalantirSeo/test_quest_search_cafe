from selenium.webdriver.common.by import By
from base.BasePage import BasePage


class GoogleSearchLocators:
    SEARCH_FIELD = (By.NAME, "q")
    SEARCH_BUTTON = (By.NAME, "btnK")


class GooglePage(BasePage):
    BASE_URL = "https://www.google.com/"

    def enter_word(self, word):
        search_field = self.find_element(GoogleSearchLocators.SEARCH_FIELD)
        search_field.click()
        search_field.send_keys(word)
        return search_field

    def click_on_the_search_button(self):
        return self.find_element(GoogleSearchLocators.SEARCH_BUTTON, time=2).click()

    def find_elements_by_xpath(self, locator):
        return self.find_elements((By.XPATH, locator), time=10)

    def find_element_by_xpath(self, locator):
        return self.find_element((By.XPATH, locator), time=10)