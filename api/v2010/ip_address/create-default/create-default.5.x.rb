# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

ip_address = @client.sip
  .ip_access_control_lists('ALaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
  .ip_addresses
  .create(friendly_name: 'friendly_name', ip_address: 'ip_address')

puts ip_address.sid
