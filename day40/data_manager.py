import requests
import os
from dotenv import load_dotenv

load_dotenv()

SHEETY_PRICE_ENDPOINT = os.getenv('SHEETY_PRICE_ENDPOINT')
SHEETY_USERS_ENDPOINT = os.getenv('SHEETY_USERS_ENDPOINT')

class DataManager:
    #This class is responsible for talking to the Google Sheet.
    def __init__(self):
        self.destination_data = {}
    
    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICE_ENDPOINT)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data
    
    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICE_ENDPOINT}/{city["id"]}",
                json=new_data
            )
            print(response.text)

    def get_coustomer_emails(self):
        customer_endpoint = SHEETY_USERS_ENDPOINT
        response = requests.get(url=customer_endpoint)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data