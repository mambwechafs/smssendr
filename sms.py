from twilio.rest import Client 
 
account_sid = 'AC88ec45fc543afc69a91560d3921af980' 
auth_token = 'ece145543eab8667bee532d60b8666d9'
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG2568d4c4d29ac728b0eedee2d7dfdb19', 
                              body='I cant believe this works',      
                              to='+260963777748' 
                          ) 
 
print(message.sid)