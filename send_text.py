from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "????????"
# Your Auth Token from twilio.com/console
auth_token  = "????????????"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+01234567890", #who you wanna send to
    from_="+01234567890", #twilio number
    body="Send a Message")  #what you want to send

print(message.sid)
