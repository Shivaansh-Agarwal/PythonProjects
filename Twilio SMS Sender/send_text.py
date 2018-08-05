from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC6c888236aacbf1fe5d289d36727d9f03"
# Your Auth Token from twilio.com/console
auth_token  = "e2e640b516a96ec17b27ad880172XXXX"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+918755297XXX", 
    from_="+12563986XXX",
    body="Hello this is Shivaansh")

print(message.sid)
