# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

origination_url = client.trunking \
    .trunks("TRaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
    .origination_urls("OUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
    .update(weight=1)

print(origination_url.sid)
