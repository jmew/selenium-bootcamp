from BasePage import *
from automation.data.Urls import *

class SignInPage(BasePage):
    url = Sign_In_Url

    def setUsername(self, UserId):
        self.waitForPageToLoadAndType(By.ID, "userId", UserId)

    def setPassword(self, Password):
        self.waitForPageToLoadAndType(By.ID, "password", Password)

    def rememberMyUserId(self):
        self.waitForPageToLoadAndClick(By.CSS_SELECTOR, "label[for='bmoCheckbox']")

    def clickForgotPassword(self):
        self.waitForPageToLoadAndClick(By.ID, "forgotPassword")

    def clickSignUp(self):
        self.waitForPageToLoadAndClick(By.ID, "signUpButton")

    def clickSecondarySignUp(self):
        self.waitForPageToLoadAndClick(By.ID, "signUpLink")

    def setLanguange(self, language):
        self.waitForPageToLoadAndClick(By.ID, "btnLanguage")
        self.waitForPageToLoadAndClick(By.CSS_SELECTOR, "button[translate='nav.language-" + language.lower() + "'")

    def submit(self):
        self.waitForPageToLoadAndClick(By.CSS_SELECTOR, "button[title='submit button title']")