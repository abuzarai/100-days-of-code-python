from bs4 import BeautifulSoup
import requests
import os
from time import sleep
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from itertools import zip_longest

http_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:127.0) Gecko/20100101 Firefox/127.0",
    "Accept-Language": "en-US, en;q=0.5",
}

load_dotenv()
response = requests.get(url=os.getenv("URL"), headers=http_headers)
soup = BeautifulSoup(response.text, "html.parser")
search_results = soup.find("div", {"id":"grid-search-results"})

def get_links():
    links_list = [a["href"] for a in search_results.find_all("a", tabindex="0")]
    for index in range(len(links_list)):
        if not links_list[index].startswith("https"):
            links_list[index] = "https://www.zillow.com" + links_list[index]
        return links_list
    
def get_address():
    address_list = [address.text for address in search_results.find_all("address")]
    return address_list

def get_price():
    price_list = [price.getText() for price in soup.find_all("div", class_="list-card-price")]
    return price_list


GOOGLE_FORM = os.getenv("FORM_URL")

service = Service('chromedriver.exe')
driver = webdriver.Chrome(service=service)
driver.get(GOOGLE_FORM)

sleep(5)


for fill_out, (address, price, link) in enumerate(zip_longest(get_address(), get_price(), get_links()), start=1):
    address = address or ""
    price = price or ""
    link = link or ""

    property_address = driver.find_element(By.XPATH, '//*[@aria-describedby = "i2 i3"]')
    property_address.send_keys(address)

    property_price = driver.find_element(By.XPATH, '//*[@aria-describedby = "i6 i7"]')
    property_price.send_keys(price)

    property_link = driver.find_element(By.XPATH, '//*[@aria-describedby = "i10 i11"]')
    property_link.send_keys(link)

    submit_button = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div')
    submit_button.click()

    another_response = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    another_response.click()

driver.quit()
