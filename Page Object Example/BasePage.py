from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from automation.data.Data import *
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException

class BasePage(object):
    url = None

    def __init__(self, driver):
        self.driver = driver

    def waitUntil(self, matcher, key):
        try:
            WebDriverWait(self.driver, Timeout).until(EC.visibility_of_element_located((matcher, key)))
        except TimeoutException:
            raise TimeoutException("Matcher: %s Key: %s not found!", str(matcher), str(key))

    def waitForPageToLoadAndClick(self, matcher, key):
        try:
            WebDriverWait(self.driver, Timeout).until(EC.presence_of_element_located((matcher, key))).click()
        except TimeoutException:
            raise TimeoutException("Matcher: %s Key: %s not found!", str(matcher), str(key))

    def waitForPageToLoadAndType(self, matcher, key, text):
        try:
            WebDriverWait(self.driver, Timeout).until(EC.presence_of_element_located((matcher, key))).send_keys(text)
        except TimeoutException:
            raise TimeoutException("Matcher: %s Key: %s not found!", str(matcher), str(key))

    def clickWereHereToHelpButton(self):
        try:
            WebDriverWait(self.driver, Timeout).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div[ng-click='openLiveChat()']"))).click()
        except TimeoutException:
            raise TimeoutException("Were here to help button not found")

    def navigate(self):
        self.driver.get(self.url)