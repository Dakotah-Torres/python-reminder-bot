import os
import smtplib
from email.message import EmailMessage

from dotenv import load_dotenv

load_dotenv() # This will load my enviornment variables

email_address       = os.getenv("MY_EMAIL")
email_app_pass      = os.getenv("MY_APP_PASSWORD")
my_phone_number     = os.getenv("MY_PHONE_NUMBER")
to_number           = my_phone_number+"@tmomail.net"
message_body        = "This is my first test message"

msg = EmailMessage()
msg.set_content(message_body)
msg['From'] = email_address
msg["To"] = to_number

with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    print("Logging in with:", email_address)
    smtp.login(email_address,email_app_pass)
    smtp.send_message(msg)



print("Sent the message")