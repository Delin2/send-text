from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC196257a4ec2327393d7d3173bd711d57"
# Your Auth Token from twilio.com/console
auth_token  = "613e599fdcf82d3661adbee14f73cb5e"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+16467611839", 
    from_="+19177460026",
    body="Shhhhhhhhhh")

print(message.sid)
