// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
const accountSid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

client.preview.sync.services('ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
      .documents('ETaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
      .documentPermissions('identity')
      .update({read: true, write: true, manage: true})
      .then(document_permission => console.log(document_permission.accountSid))
      .done();
