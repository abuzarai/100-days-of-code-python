import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

MAIL_PROVIDER_SMTP_ADDRESS = "smtp.gmail.com"
MY_EMAIL = os.getenv('EMAIL')
MY_PASSWORD = os.getenv('PASSWORD')

class NotificationManager:
    #This class is responsible for sending notifications with the deal flight details.
    def email_sender(self, emails, message, google_flight_link):
        with smtplib.SMTP(MAIL_PROVIDER_SMTP_ADDRESS) as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            for email in emails:
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=email,
                    msg=f"Subject:New low price flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
        
        