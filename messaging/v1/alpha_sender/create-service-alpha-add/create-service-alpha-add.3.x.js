// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
const accountSid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

client.messaging.services('MGaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                .alphaSenders
                .create({alphaSender: 'My company'})
                .then(alpha_sender => console.log(alpha_sender.sid))
                .done();
