import smtplib

email = input("Enter your gmail username: ") + '@gmail.com'
another_email = "another_fake_paula@yahoo.com"
password = input("Enter your password: ")

connection = smtplib.SMTP("smtp.gmail.com", port=587)
connection.starttls()
connection.login(user=email, password=password)
connection.sendmail(from_addr=email, to_addrs=another_email, msg="Hello!")
connection.close()
