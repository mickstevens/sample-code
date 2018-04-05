# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

document_permission = @client.sync
                             .services('ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                             .documents('ETaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                             .document_permissions('identity')
                             .update(manage: true, read: true, write: true)

puts document_permission.account_sid
