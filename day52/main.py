from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep

USERNAME = "username"
PASSWORD = 'password'

TARGET_ACCOUNT = "username" # enter the account you want to follow the audience of

class InstaBot:
    def __init__(self) -> None:
        self.driver = webdriver.Chrome(service='chromedriver.exe')
    
    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        sleep(5)
        username_input = self.driver.find_element(By.NAME, 'username')
        username_input.clear()
        username_input.send_keys(USERNAME)
        password_input = self.driver.find_element(By.NAME, 'password')
        password_input.clear()
        password_input.send_keys(PASSWORD)
        sleep(5)
        password_input.send_keys(Keys.ENTER)

        def find_followers(self):
            sleep(5)
            self.driver.get(f'https://www.instagram.com/{TARGET_ACCOUNT}/')
            sleep(3)
            followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/div[3]/ul/li[2]/div/button')
            followers.click()

            sleep(3)

            modal = self.drier.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')
            for i in range(10):
                self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
                sleep(2)

        def follow(self):
            all_buttons = self.driver.find_elements(By.CSS_SELECTOR, 'li button')
            for button in all_buttons:
                try:
                    button.click()
                    sleep(1)
                except ElementClickInterceptedException:
                    cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                    cancel_button.click()


bot = InstaBot()
bot.login()
bot.find_followers()
bot.follow()
