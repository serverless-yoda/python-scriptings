import smtplib
from email.message import EmailMessage
import configparser
from string import Template
from pathlib import Path

# read config
config = configparser.ConfigParser()
config.read('config.conf')
emailAccount = config['default']['emailAccount']
emailPassword = config['default']['emailPassword']
toDestination = config['default']['toDestination']
fromSender = config['default']['fromSender']

# read index.html and convert to template
html = Template(Path('index.html').read_text())


# create object
email = EmailMessage()
email['from'] = emailAccount
email['to'] = toDestination
email['subject'] = 'This is a test email from python'

# use the template and substitute and
# set it to html
email.set_content(html.substitute({'name': 'Anaconda'}), 'html')

# send
with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(emailAccount, emailPassword)
    smtp.send_message(email)
