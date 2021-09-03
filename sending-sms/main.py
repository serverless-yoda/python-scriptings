import configparser
from twilio.rest import Client

parser = configparser.ConfigParser()
parser.read('config.conf')

 
account_sid = parser.get('default','twillio_sid')
auth_token = parser.get('default','twillio_token')
messaging_service_sid = parser.get('default','twillio_full_phonenumber')
destination_phone = parser.get('default','destination_phone')
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid=messaging_service_sid, 
                              body='this is a test',      
                              to=destination_phone 
                          ) 
 
print(message.sid)
