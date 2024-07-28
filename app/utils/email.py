import smtplib
from email.mime.text import MIMEText
import os

def send_email(to_email, subject, body):
    from_email = os.getenv("SMTP_MAIL")
    password = os.getenv("SMTP_PASSWORD")

    print("Checking email credentials")

    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = from_email
    msg['To'] = to_email

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(from_email, password)
    server.sendmail(from_email, to_email, msg.as_string())
    server.quit()
