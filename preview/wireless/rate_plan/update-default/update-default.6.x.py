# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

rate_plan = client.preview.rate_plans("WPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
                          .update(unique_name="unique_name")

print(rate_plan.sid)
