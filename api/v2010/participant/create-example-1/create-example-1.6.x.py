# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

participant = client.conferences("CFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                    .participants \
                    .create(from_="+18180021216", to="+15624421212")

print(participant.account_sid)
