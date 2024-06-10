import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_emailID = input("Enter your email id: ")
password = input("Enter your password: ")
receiver_emailID = input("Enter receiver's email id: ")
subject = input("Enter the subject of the email: ")
text = input("Enter the body of the email: ")
body = MIMEMultipart()
body['Subject'] = subject
body.attach(MIMEText(text))

smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(sender_emailID, password)
smtpObj.sendmail(sender_emailID, receiver_emailID, body.as_string())
smtpObj.quit()
