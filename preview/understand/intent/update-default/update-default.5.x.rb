# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

intent = @client.preview.understand
                        .services('UAaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                        .intents('UDaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                        .update(friendly_name: 'friendly_name')

puts intent.sid
