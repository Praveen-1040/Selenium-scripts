import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Import the correct Keys module
from selenium.webdriver.chrome.options import Options

# Initialize WebDriver
chrome_options = Options()
chrome_options.add_argument("--incognito")

browser = webdriver.Chrome(options=chrome_options)
browser.maximize_window()

groww_url = "https://groww.in/"

browser.get(groww_url)

cmpny_name = "TATA MOTORS"
# Click on search 
search_field = browser.find_element(By.ID,value="globalSearch23")
search_field.send_keys(cmpny_name)
search_field.send_keys(Keys.ENTER)

first_option = browser.find_element(By.CSS_SELECTOR,value=".se28Suggestions .fsAuto")
first_option.click()
time.sleep(10)




