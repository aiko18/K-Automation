import pytest
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestSearchField:
    driver = ""

    def setup_method(self):
        email = "aida.taymaskhanova@testpro.io"
        password = "Ozzikpozzik18"
        path = "C:\\Program Files (x86)\\chromedriver.exe"
        options = webdriver.ChromeOptions()
        options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(options=options)
        self.driver.get("https://qa.koel.app")
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        print(self.driver.title)
        # log in
        self.driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    # verify the search box is present on the page
    def test_searchBox_is_present(self):
        search_box = self.driver.find_element(By.XPATH, "//input[@type='search']")
        time.sleep(5)
        if search_box.is_displayed():
            print("Search Box is present")
        assert search_box, "search box is not present"

    @pytest.mark.parametrize("search_query", ["reactor", "Ketsa", "Dark Days"])
    def test_relevant_search(self, search_query):
        search_box = self.driver.find_element(By.XPATH, "//input[@type='search']")
        search_box.send_keys(search_query)
        search_box.click()
        time.sleep(5)
        search_result = self.driver.find_elements(By.XPATH, "//div[@class='results']//ul")
        for r in search_result:
            print(r.text)


    def teardown_method(self):
        self.driver.quit()
