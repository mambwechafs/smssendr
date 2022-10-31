#pip install twilio
from twilio.rest import Client 
 
account_sid = '' #enter account sid
auth_token = ' ' #enter auth token
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='', 
                              body=' ',      
                              to='   ' 
                          ) #enter messaging service id, the message and the phone number you are sending to
 
print(message.sid)
