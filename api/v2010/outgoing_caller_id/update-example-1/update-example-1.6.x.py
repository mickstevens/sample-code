# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

outgoing_caller_id = client \
    .outgoing_caller_ids("PNaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
    .update(friendly_name="My Second Line")

print(outgoing_caller_id.sid)
