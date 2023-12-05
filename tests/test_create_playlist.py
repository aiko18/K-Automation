import pytest
from selenium import webdriver
import time
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class TestPlaylist:
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
        print(self.driver.title)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    @pytest.mark.parametarise("name", ["My_list"])
    def test_create_playlist(self,name):

        create_playlist = self.driver.find_element(By.CSS_SELECTOR, "[title = 'Create a new playlist']")
        create_playlist.click()
        time.sleep(3)
        new_playlist = self.driver.find_element(By.CSS_SELECTOR,
                                                "li[data-testid='playlist-context-menu-create-simple']")
        new_playlist.click()
        time.sleep(5)
        playlist_name = self.driver.find_element(By.XPATH, "//input[@name='name']")
        time.sleep(4)
        playlist_name.send_keys(name)
        playlist_name.send_keys(Keys.ENTER)
        time.sleep(5)

        pop_up_notification = self.driver.find_element(By.XPATH,
                                                       "//div[@class='alertify-logs top right']/div[@class='success "
                                                       "show']")

        assert pop_up_notification, "No notification popped out"
        expected_text = f"Created playlist {name}"
        assert pop_up_notification == f"Expected text{expected_text}"


    def teardown_method(self):
        self.driver.quit()
