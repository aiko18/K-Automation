from selenium import webdriver
import time
import pytest
from selenium.webdriver.common.by import By


class TestHomePage:
    driver = ""

    def setup_method(self):
        email = "aida.taymaskhanova@testpro.io"
        password = "Ozzikpozzik18"
        path = "C:\\Program Files (x86)\\chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://qa.koel.app")
        self.driver.implicitly_wait(10)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(email)

        self.driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def test_home_sidebar(self):
        home_section = self.driver.find_element(By.XPATH, "//section[@class='music']//h1")
        print(home_section.text)
        home_test_display = self.driver.find_elements(By.XPATH, "//section[@class='music']//li//a")
        for i in home_test_display:
            print(i.text)

        playlist_section = self.driver.find_element(By.XPATH, "//section[@id='playlists']/h1")
        print(playlist_section.text)
        playlist_display = self.driver.find_elements(By.XPATH, "//section[@id='playlists']//ul//li")
        for m in playlist_display:
            print(m.text)

    def teardown_method(self):
        self.driver.quit()
