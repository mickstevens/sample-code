# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

fax = @client.fax.faxes
  .create(
     media_url: 'https://www.twilio.com/docs/documents/25/justthefaxmaam.pdf',
     to: 'sip:kate@example.com',
     from: 'Jack',
     sip_auth_password: 'secret',
     sip_auth_username: 'jack'
   )

puts fax.sid
