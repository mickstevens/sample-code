// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
const accountSid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

client.calls
      .create({
         from: '+15017122661',
         to: '+15558675310',
         url: 'http://demo.twilio.com/docs/voice.xml'
       })
      .then(call => console.log(call.sid))
      .done();
