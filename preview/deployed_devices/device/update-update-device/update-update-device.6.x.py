# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

device = client.preview.deployed_devices \
                       .fleets("FLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                       .devices("THaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                       .update(
                            friendly_name="My New Device",
                            identity="bob@twilio.com"
                        )

print(device.sid)
