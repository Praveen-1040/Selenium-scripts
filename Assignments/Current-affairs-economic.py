from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

news_url = "https://currentaffairs.adda247.com/economy-current-affairs/"
driver.get(news_url)

# Give the page some time to load
time.sleep(5)

# Find all the news links inside the specified <ul> element
news_links = driver.find_elements(By.XPATH, value="//li[@class='category_postlist']//div[@class='desc']/a")

all_links = []
for link in news_links:
    href = link.get_attribute("href")
    if href:
        all_links.append(href)

print("Total links found:", len(all_links))

# List to store key points
all_key_points = []

# Iterate through each link
for link in all_links:
    # Open a new tab
    driver.execute_script("window.open('about:blank', '_blank');")
    time.sleep(1)

    # Switch to the new tab and open the new URL
    driver.switch_to.window(driver.window_handles[-1])
    driver.get(link)

    # Give the page some time to load
    time.sleep(5)

    # Extract the second column (<td> tags with style "width: 69.2121%")
    key_points = driver.find_elements(By.XPATH, value='//td[@style="width: 69.2121%"]')

    # Append each key point to the list
    for point in key_points:
        all_key_points.append(point.text)

    # Close the current tab and switch back to the main tab
    driver.close()
    driver.switch_to.window(driver.window_handles[0])

# Save key points to a text file
with open("key_points.txt", "w", encoding="utf-8") as file:
    for index, point in enumerate(all_key_points, start=1):
        file.write(f"{index}. {point}\n")

print("Key points saved to 'key_points.txt'")

# Close the browser
driver.quit()
