// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
const accountSid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

client.preview.marketplace
  .availableAddOns('XBaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
  .extensions('XFaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
  .fetch()
  .then(available_add_on_extension => console.log(available_add_on_extension.sid))
  .done();
