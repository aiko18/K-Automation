from selenium import webdriver
import time
from selenium.common import NoAlertPresentException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains

path = "C:\\Program Files (x86)\\chromedriver.exe"
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=options)
action = ActionChains(driver)
driver.get("https://qa.koel.app")
driver.maximize_window()
driver.implicitly_wait(10)

user = driver.find_element(By.CSS_SELECTOR, "input[type='email']")
user.send_keys('aida.taymaskhanova@testpro.io')
password_locator = driver.find_element(By.CSS_SELECTOR, "input[type='password']")
password_locator.send_keys('Ozzikpozzik18')
button_submit = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
button_submit.click()
time.sleep(3)
print(driver.current_url)
time.sleep(10)

# Pop out notification

try:
    # switch to alert and click ok button
    driver.switch_to.alert.dismiss()
except NoAlertPresentException:
    print("exception handled")

print("Rest of the program")

your_music = driver.find_element("xpath", "//section[@class='music']/h1")
playlists = driver.find_element(By.CSS_SELECTOR, "#playlists h1")
print(your_music.text)
print(playlists.text)
left_sidebar = driver.find_elements("xpath", "//nav[@id='sidebar']//a")
for i in left_sidebar:
    print(i.text)
    print(len(left_sidebar))

time.sleep(7)

greetings = driver.find_element(By.XPATH, "//div[@class='heading-wrapper']//h1")
print(greetings.is_displayed())
print(greetings.get_attribute("value"))

time.sleep(2)

# create a playlist
create_playlist = driver.find_element(By.CSS_SELECTOR, "[title = 'Create a new playlist']")
create_playlist.click()
time.sleep(3)
new_playlist = driver.find_element(By.CSS_SELECTOR, "li[data-testid='playlist-context-menu-create-simple']")
new_playlist.click()
playlist_name = driver.find_element(By.XPATH, "//input[@name='name']")
time.sleep(4)
playlist_name.send_keys("My_list")
playlist_name.send_keys(Keys.ENTER)
time.sleep(3)

# verify there is a pop out after creating a playlist. The selector is wrong here.
# pop_out = driver.find_element("XPATH", "//div[@class='success show']")
# print(pop_out.text)


# delete an existing playlist
my_playlist = driver.find_element("xpath", "//a[@href='#!/playlist/77075']")

# right click
action.context_click(my_playlist).perform()
time.sleep(5)

# delete created playlist
delete_button = driver.find_element("xpath", "//li[@data-testid='playlist-context-menu-delete-77075']")
delete_button.click()
time.sleep(4)


# rename playlist

# enter new name into the field of the playlist
# new_name = driver.find_element(By.CSS_SELECTOR, "[href='#!/playlist/77050']")
# time.sleep(6)
# new_name.send_keys(Keys.CONTROL,'a')
# time.sleep(10)
# new_name.send_keys(Keys.DELETE)
# time.sleep(10)
# new_name.send_keys("new_list")

# rename_playlist.send_keys("New_List")
# rename_playlist.click()


driver.quit()
