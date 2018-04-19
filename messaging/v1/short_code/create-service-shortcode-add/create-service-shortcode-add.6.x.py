# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

short_code = client.messaging.services("MGXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX") \
                   .short_codes \
                   .create(short_code_sid="SC3f94c94562ac88dccf16f8859a1a8b25")

print(short_code.sid)
