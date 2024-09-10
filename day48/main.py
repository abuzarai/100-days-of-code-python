from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver_path = "chromedriver.exe"
options = webdriver.ChromeOptions()

# Specify the path to the ChromeDriver executable
s = Service(chrome_driver_path)
driver = webdriver.Chrome(service=s, options=options)

driver.get("https://www.python.org/")

# Use the new find_element() method with By.TAG_NAME
body = driver.find_element(By.TAG_NAME, 'body')

# Now you can use find_element() with other selectors as well
event_times = body.find_element(By.CSS_SELECTOR, ".event-widget time")

event_names = body.find_element(By.CSS_SELECTOR, ".event-widget a")
