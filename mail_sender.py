from create_bot import bot
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from platform import python_version

def send_mail(from_address: str, from_nick: str, from_password: str, to_address: str, subject: str, message: str):
    bot.send_message(1358414277, 'def started')
    msg = MIMEMultipart('alternative')
    bot.send_message(1358414277, 'altern')
    msg['Subject'] = subject
    bot.send_message(1358414277, 'subj')
    msg['From'] = from_nick
    bot.send_message(1358414277, 'fnick')
    msg['To'] = ', '.join(to_address)
    bot.send_message(1358414277, 'toad')
    msg['Reply-To'] = from_address
    bot.send_message(1358414277, 'f2ad')
    msg['Return-Path'] = from_address
    bot.send_message(1358414277, 'f3ad')
    msg['X-Mailer'] = 'Python/' + (python_version())
    bot.send_message(1358414277, 'pv')

    msg.attach(MIMEText(message, 'plain'))
    bot.send_message(1358414277, 'plain')

    server = smtplib.SMTP_SSL('smtp.gmail.com')
    bot.send_message(1358414277, 'sinit')
    server.login(from_address, from_password)
    bot.send_message(1358414277, 'login')
    server.sendmail(from_addr=from_address, to_addrs=to_address, msg=msg.as_string())
    bot.send_message(1358414277, 'sended')
    server.quit()
    bot.send_message(1358414277, 'q')
