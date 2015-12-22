import unittest

from selenium import webdriver

from automation.helperMethods.SignUpMethods import *

class SignInTests(unittest.TestCase):

    def setUp(self):
         self.UserID = str(time.time())[:-3]
         self.driver = Driver

    def test_Sign_In_Required_Information_verify_Username_And_Password_Elements(self):
        driver = self.driver
        signInPage = SignInPage(driver)
        signInPage.navigate()
        assert waitUntil(driver, Timeout, By.CSS_SELECTOR, "label[for='userId']")
        assert waitUntil(driver, Timeout, By.NAME, 'userId').get_attribute('placeholder') == 'User ID'
        assert waitUntil(driver, Timeout, By.CSS_SELECTOR, "label[for='password']")
        assert waitUntil(driver, Timeout, By.NAME, 'password').get_attribute('placeholder') == 'Password'

    def test_Sign_In_Error_Handling_verify_Error_Is_Shown(self):
        driver = self.driver
        signInPage = SignInPage(driver)
        signInPage.navigate()
        signInPage.submit()
        assert waitUntil(driver, Timeout, By.CSS_SELECTOR, "span[translate='login.no-value-message']")
        assert waitUntil(driver, Timeout, By.ID, 'loginErrorMsg')

    def test_Sign_In_Forgot_Password_verify_Link_Takes_You_To_The_Forgot_Password_Page(self):
        driver = self.driver
        signInPage = SignInPage(driver)
        signInPage.navigate()
        signInPage.clickForgotPassword()
        assert waitUntil(driver, Timeout, By.CSS_SELECTOR, "h1[translate='reset.title']")

    def test_Sign_In_Remember_My_User_Id_verify_Id_Is_Saved(self):
        driver = self.driver
        signIn(driver, '144675051', 'Xtreme234')
        waitForPageToLoadAndClick(driver, By.CLASS_NAME, 'dropdown')
        waitForPageToLoadAndClick(driver, By.CSS_SELECTOR, "a[translate='nav.dropdown.signOut']")
        waitUntil(driver, Timeout, By.NAME, 'userId')
        assert waitUntil(driver, Timeout, By.NAME, 'userId').get_attribute('value') == '144675051'
        assert WebDriverWait(driver, Timeout).until(EC.presence_of_element_located((By.ID, 'bmoCheckbox'))).is_selected()

    def tearDown(self):
        self.driver.quit()