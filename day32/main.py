import datetime as dt
import pandas as pd
import random
import smtplib
from email.message import EmailMessage

def send_email(to_email, subject, message, from_email, password):
        msg = EmailMessage()
        msg['Subject'] = subject
        msg['From'] = from_email
        msg['To'] = to_email
        msg.set_content(message)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as server:
            server.login(from_email, password)
            server.send_message(msg)

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pd.read_csv('birthdays.csv')
birthdays_dict = {(row['month'], row['day']): row for _, row in data.iterrows()}

if today_tuple in birthdays_dict:
    person = birthdays_dict[today_tuple]['name']
    person_email = birthdays_dict[today_tuple]['email']

    letter_template_number = random.randint(1, 3)
    letter_template_file = f"letter_templates/letter_{letter_template_number}.txt"

    with open(letter_template_file, 'r') as file:
        letter_content = file.read()
        modified_letter_content = letter_content.replace("[NAME]", person)
        print(modified_letter_content) 

        send_email(
            to_email=person_email,
            subject="Happy birthday!",
            message=modified_letter_content,
            from_email='youremail@gmail.com',
            password= "yourpassword"
        )
    