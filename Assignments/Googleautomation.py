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

# Open the URL
login_url = "https://www.google.co.in/"
browser.get(login_url)

# Define credentials
gmail_name = "praveennm1976@gmail.com"
password = "indiaismycountry"

# Click on "Sign in"
time.sleep(5)
browser.find_element(By.XPATH, "//a[@aria-label='Sign in']").click()

# Enter Gmail ID
time.sleep(10)
gmail_field = browser.find_element(By.XPATH, "//input[@id='identifierId']")
gmail_field.send_keys(gmail_name)  # Correct usage of send_keys
gmail_field.send_keys(Keys.ENTER)  # Send Enter key

# Enter Password
time.sleep(10)
password_field = browser.find_element(By.XPATH, "//input[@name='Passwd']")
password_field.send_keys(password)  # Correct usage of send_keys
password_field.send_keys(Keys.ENTER)  # Send Enter key

# Handle Alert Box (if present)
time.sleep(10)
try:
    alertbox = browser.switch_to.alert
    alertbox.dismiss()
except Exception as e:
    print("No alert box found:", e)

# Add any further steps here
time.sleep(10)
browser.quit()
