import smtplib
import sys
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Replace input command with your email address
sender_emailID = input("Enter your email id: ")
# Replace inout command with you password/app specific password
password = input("Enter your password: ")
receiver_emailID = input("Enter receiver's email id: ")
subject = input("Enter the subject of the email: ")
print("Enter the body of the email, press crtl + D once finished: ")
text = sys.stdin.read()
body = MIMEMultipart()
body['Subject'] = subject
body.attach(MIMEText(text))

smtpObj = smtplib.SMTP("smtp.gmail.com", 587)
smtpObj.ehlo()
smtpObj.starttls()
smtpObj.login(sender_emailID, password)
smtpObj.sendmail(sender_emailID, receiver_emailID, body.as_string())
smtpObj.quit()
