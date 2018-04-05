# Download the helper library from https://www.twilio.com/docs/ruby/install
require 'rubygems'
require 'twilio-ruby'

# Your Account Sid and Auth Token from twilio.com/console
account_sid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa'
auth_token = 'your_auth_token'
@client = Twilio::REST::Client.new(account_sid, auth_token)

add_on_results = @client.recordings('REaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                        .add_on_results
                        .list

add_on_results.each do |record|
  puts record.sid
end
