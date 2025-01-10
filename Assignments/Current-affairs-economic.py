from selenium.webdriver.chrome.options import Options
from selenium import webdriver
import time
from selenium.webdriver.common.by import By

# Initialize WebDriver
driver = webdriver.Chrome()
driver.maximize_window()

# URL of the news page
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

# Open a file to write the extracted key points
with open("New_key_points.txt", "w", encoding="utf-8") as file:
    # Iterate through each link
    for index, link in enumerate(all_links, start=1):
        # Open a new tab
        driver.execute_script("window.open('about:blank', '_blank');")
        time.sleep(1)

        # Switch to the new tab and open the new URL
        driver.switch_to.window(driver.window_handles[-1])
        driver.get(link)

        # Give the page some time to load
        time.sleep(5)

        # Scroll down to ensure the table is visible
        driver.execute_script("window.scrollBy(0, 800);")
        time.sleep(2)

        # Extract the heading from the <h1> tag
        try:
            heading = driver.find_element(By.XPATH, "//h1[@class='entry-title']").text
        except Exception as e:
            heading = "Heading not found"
            print(f"Error extracting heading: {e}")

        # Locate the rows of the table
        rows = driver.find_elements(By.XPATH, "//table//tr")

        # Extract data from the second column of each row (skip header row)
        key_points = []
        for row in rows[1:]:
            try:
                second_cell = row.find_element(By.XPATH, "./td[2]")
                key_points.append(second_cell.text)
            except Exception as e:
                print(f"Could not extract data for a row: {e}")

        # Write the extracted data to the file
        file.write(f"News Heading: {heading}\n")
        if key_points:
            for point_num, point in enumerate(key_points, start=1):
                file.write(f"{point_num}. {point}\n")
        else:
            file.write("No key points found.\n")
        file.write("\n")  # Add a blank line between articles

        # Close the current tab and switch back to the main tab
        driver.close()
        driver.switch_to.window(driver.window_handles[0])

print("Key points and headings have been saved to 'New_key_points.txt'.")

# Close the browser
driver.quit()
