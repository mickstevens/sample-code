# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = '"ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url="http://www.example.com/sipdial.xml",
                        from_="Jack",
                        to="sip:kate@example.com?hatchkey=4815162342"
                    )

print(call.sid)
