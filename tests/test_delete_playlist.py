from selenium import webdriver


from selenium.webdriver.common.by import By

from tests.test import action


class TestDeletePlaylist:
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
        # log in
        self.driver.find_element(By.CSS_SELECTOR, "input[type='email']").send_keys(email)
        self.driver.find_element(By.CSS_SELECTOR, "input[type='password']").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "button[type='submit']").click()

    def test_delete_playlist(self):
        my_playlist = self.driver.find_element("xpath", "//a[@href='#!/playlist/77075']")

        # right click
        action.context_click(my_playlist).perform()
        delete_button = self.driver.find_element("xpath", "//li[@data-testid='playlist-context-menu-delete-77075']")
        delete_button.click()
        pop_up_notification = self.driver.find_element(By.XPATH,
                                                       "//div[@class='alertify-logs top right']/div[@class='success show']")
        assert pop_up_notification, "No notification popped out"

    def teardown_method(self):
        self.driver.quit()
