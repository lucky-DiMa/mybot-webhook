import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from platform import python_version

def send_mail(from_address: str, from_nick: str, from_password: str, to_address: str, subject: str, message: str):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = from_nick
    msg['To'] = ', '.join(to_address)
    msg['Reply-To'] = from_address
    msg['Return-Path'] = from_address
    msg['X-Mailer'] = 'Python/' + (python_version())

    msg.attach(MIMEText(message, 'plain'))

    server = smtplib.SMTP_SSL('smtp.gmail.com')
    server.login(from_address, from_password)
    server.sendmail(from_addr=from_address, to_addrs=to_address, msg=msg.as_string())
    server.quit()
