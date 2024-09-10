from selenium import webdriver
from selenium.webdriver.chrome import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException 
import time

EMAIL = "**************"
PASSWORD = "*********"
PHONE_NUMBER = "*************"

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get("https://www.linkedin.com/jobs/search/?f_AL=true&geoId=101174742&keywords=Analytic%20Recruiting%20Inc&location=Australia")

# Sign in

driver.find_element(By.LINK_TEXT, "Sign In").click()
time.sleep(5)

email = driver.find_element(By.NAME, "session_key")
email.send_keys(EMAIL)
password = driver.find_element(By.NAME, "session_password")
password.send_keys(PASSWORD)
time.sleep(10)

# Find jobs

jobs = driver.find_element(By.CLASS_NAME, 'job-card-list__title')
available_jobs = [job.text for job in jobs]

while available_jobs:
    posting_num = 0
    try:
        driver.find_element(By.LINK_TEXT, f'{available_jobs[posting_num]}').click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, 'jobs-s-apply').click()
    except NoSuchElementException:
        posting_num += 1
        driver.find_element(By.LINK_TEXT, f'{available_jobs[posting_num]}').click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, 'jobs-s-apply').click()
    finally: # fill form
        available_jobs.remove(available_jobs[posting_num])
        try:
            time.sleep(2)
            phone_number = driver.find_element(By.CLASS_NAME, 'fb-single=line-text__input')
            phone_number.clear()
            time.sleep(2)
            phone_number.send_keys(PHONE_NUMBER)
            driver.find_element(By.CSS_SELECTOR, 'footer button').click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Review your application"]').click()
            time.sleep(2)
            driver.find_element(By.CSS_SELECTOR, '[aria-label="Submit application"]').click()
        except NoSuchElementException:
            print("Can't apply, skipped!")
        break