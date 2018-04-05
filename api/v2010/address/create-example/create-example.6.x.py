# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

address = client.addresses.create(
                               city="Racoon",
                               customer_name="Customer 500",
                               iso_country="AX",
                               postal_code="150",
                               region="Mordor",
                               street="Elm Street"
                           )

print(address.sid)
