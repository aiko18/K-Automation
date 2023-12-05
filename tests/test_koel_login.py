from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


class TestKoelLogin:
    driver = ""

    def setup_method(self):
        path = "C:\\Program Files (x86)\\chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://qa.koel.app")
        self.driver.implicitly_wait(10)
        print(self.driver.title)

    @pytest.mark.login
    @pytest.mark.parametrize("user_name, password, actual_url", [("aida.taymaskhanova@testpro.io", "Ozzikpozzik18", "https://qa.koel.app/#!/home")])
    def test_koel_positive_login(self, user_name, password, actual_url, ):
        # print(self.driver.title)

        user = self.driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        user.send_keys(user_name)

        password_locator = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_locator.send_keys(password)
        button_submit = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button_submit.click()
        time.sleep(3)
        print(self.driver.current_url)
        url = self.driver.current_url
        assert url == actual_url, "https://qa.koel.app/#!/home"

    # text_locator = driver.find_element(
    # print(text_locator.text)

    # assert text_locator == " Howdy, student! "

    # negative login test with incorrect username

    @pytest.mark.parametrize('user_name, password',
                             [("taymaskhan.aida@gmail.com", "Ozzikpozzik18")])
    def test_negative_username(self, user_name, password):
        user = self.driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        user.send_keys(user_name)
        password_locator = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_locator.send_keys(password)
        button_submit = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button_submit.click()
        time.sleep(3)

    @pytest.mark.parametrize('user_name, password',
                             [("taymaskhan.aida@gmail.com", "Ozzikpozzik")])
    def test_negative_password(self, user_name, password):
        user = self.driver.find_element(By.CSS_SELECTOR, "input[type='email']")
        user.send_keys(user_name)
        password_locator = self.driver.find_element(By.CSS_SELECTOR, "input[type='password']")
        password_locator.send_keys(password)
        button_submit = self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        button_submit.click()
        time.sleep(3)

    def teardown_method(self):
        self.driver.quit()
