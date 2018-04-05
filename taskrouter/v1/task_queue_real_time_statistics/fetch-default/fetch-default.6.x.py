# Download the helper library from https://www.twilio.com/docs/python/install
from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
client = Client(account_sid, auth_token)

task_queue_real_time_statistics = client.taskrouter \
    .workspaces("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
    .task_queues("WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa") \
    .real_time_statistics() \
    .fetch()

print(task_queue_real_time_statistics.account_sid)
