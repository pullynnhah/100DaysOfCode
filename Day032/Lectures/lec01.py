import smtplib
import os

email = os.environ["MY_EMAIL"]
password = os.environ["MY_EMAIL_PASSWORD"]

another_email = "another_fake_paula@yahoo.com"

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs=another_email, msg="Hello!")
connection.close()
