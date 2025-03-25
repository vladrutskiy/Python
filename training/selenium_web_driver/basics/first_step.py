from selenium import webdriver


# If the WebDriver is in PATH, you can simply do:
driver = webdriver.Chrome()

# Open a website
driver.get("https://google.com/")

# Print the page title
print(f"Page Title: {driver.title}")

# Close the browser
driver.quit()