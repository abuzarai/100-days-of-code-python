import requests
import smtplib
from email.mime.text import MIMEText
from flight_data import FlightData

flightdata = FlightData()

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def email_sender(self):

        self.msg = MIMEText(f'Low price alert! Only {flightdata.price} to fly from {flightdata.origin_city}--{flightdata.origin_airport}'
                            f"to {flightdata.destination_city}--{flightdata.destination_airport},"
                            f"from {flightdata.out_date} to {flightdata.return_date}")
        self.msg['Subject'] = '!!! Fly at low price !!!'
        self.msg['From'] = 'your_email@gmail.com'
        self.msg['To'] = 'recipient_email@example.com'

        self.s = smtplib.SMTP('smtp.gmail.com', 587)
        self.s.starttls()
        self.s.login('your_email@gmail.com', 'your_password')
        self.s.sendmail('your_email@gmail.com', ['recipient_email@example.com'], self.msg.as_string())
        self.s.quit()
        