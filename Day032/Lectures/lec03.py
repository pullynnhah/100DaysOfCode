import smtplib

email = input("Enter your gmail username: ") + '@gmail.com'
another_email = "another_fake_paula@yahoo.com"
password = input("Enter your password: ")

with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
    connection.starttls()
    connection.login(user=email, password=password)
    message = "Subject:Hello World\n\nSending e-mail with Python!!!"
    connection.sendmail(from_addr=email, to_addrs=another_email, msg=message)
