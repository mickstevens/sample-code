# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

call = @client.calls.create(
                       from: 'Jack',
                       to: 'sip:kate@example.com',
                       sip_auth_password: 'secret',
                       sip_auth_username: 'jack',
                       url: 'http://www.example.com/sipdial.xml'
                     )

puts call.sid
