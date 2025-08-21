from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Setup Chrome
options = webdriver.ChromeOptions()
options.add_argument("--start-maximized")
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

# 1. Open the site
driver.get("https://demo.testfire.net/")
time.sleep(2)
print("Opened home page")

# 2. Click on 'Sign In'
driver.find_element(By.LINK_TEXT, "Sign In").click()
time.sleep(2)
print("Clicked Sign In")

# 3. Perform login (Demo credentials from site: username=jsmith, password=demo1234)
driver.find_element(By.ID, "uid").send_keys("admin")
driver.find_element(By.ID, "passw").send_keys("admin")
driver.find_element(By.NAME, "btnSubmit").click()
time.sleep(2)
print("Logged in")

# 4. Click 'View Account Summary'
driver.find_element(By.LINK_TEXT, "View Account Summary").click()
time.sleep(2)
print("Visited Account Summary")

# 5. Click on first account link
driver.find_element(By.XPATH, "//table//a").click()
time.sleep(2)
print("Visited First Account")

# 6. Click on 'Transfer Funds'
driver.find_element(By.LINK_TEXT, "Transfer Funds").click()
time.sleep(2)
print("Visited Transfer Funds")

# 7. Click on 'Log Out'
driver.find_element(By.LINK_TEXT, "Sign Off").click()
time.sleep(2)
print("Logged Out")

# Close browser
driver.quit()
