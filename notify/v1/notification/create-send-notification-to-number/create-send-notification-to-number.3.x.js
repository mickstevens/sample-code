// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
const accountSid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

client.notify.services('ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
      .notifications
      .create({
         body: 'Knok-Knok! This is your first Notify SMS',
         toBinding: `{"binding_type":"sms", "address":"+1651000000000"}`,
         identity: ['identity']
       })
      .then(notification => console.log(notification.sid))
      .done();
