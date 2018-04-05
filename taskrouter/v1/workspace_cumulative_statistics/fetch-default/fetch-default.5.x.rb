# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

workspace_cumulative_statistics = @client.taskrouter
  .workspaces('WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
  .cumulative_statistics
  .fetch

puts workspace_cumulative_statistics.account_sid
