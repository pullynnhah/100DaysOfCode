import smtplib
import os

email = os.environ["MY_EMAIL"]
password = os.environ["MY_EMAIL_PASSWORD"]
another_email = "another_fake_paula@yahoo.com"

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    message = "Subject:Hello World\n\nSending e-mail with Python!!!"
    connection.sendmail(from_addr=email, to_addrs=another_email, msg=message)
