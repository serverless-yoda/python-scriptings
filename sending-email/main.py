import smtplib
from email.message import EmailMessage
import configparser


# read config
config = configparser.ConfigParser()
config.read('config.conf')
emailAccount = config['default']['emailAccount']
emailPassword = config['default']['emailPassword']
toDestination = config['default']['toDestination']
fromSender = config['default']['fromSender']

# create object
email = EmailMessage()
email['from'] = emailAccount
email['to'] = toDestination
email['subject'] = 'This is a test email from python'
email.set_content('Im from python program')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(emailAccount, emailPassword)
    smtp.send_message(email)
