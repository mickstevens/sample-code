# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

alpha_sender = @client.messaging.services('MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                                .alpha_senders
                                .create(alpha_sender: 'My company')

puts alpha_sender.sid
