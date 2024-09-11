from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException
from time import sleep

EMAIL = "********"
PASSWORD = "********"

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)

driver.get('https://www.tinder.com/')

sleep(5)
login_button = driver.find_element(By.XPATH, '//*[@id="o-1924464"]/div/div[1]/div/main/div[1]/div/div/div/div/header/div/div[2]/div[2]/a')
login_button.click()

sleep(5)
email_field = driver.find_element(By.NAME, "email")
email_field.send_keys(EMAIL)
password_field = driver.find_element(By.NAME, "password")
password_field.send_keys(PASSWORD)

allow_location_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
notifications_button = driver.find_element(By.XPATH, value='//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
cookies = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for i in range(100):
    sleep(1)
    try:
        like_button = driver.find_element(By.XPATH, value='//*[@id="content"]/div/div[2]/div/div/div[2]/button[3]')
        like_button.click()
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, value='.itsAMatch a')
            match_popup.click()
        except NoSuchElementException:
            sleep(2)

driver.quit()