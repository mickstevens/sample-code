// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
const accountSid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

client.notify.services('ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
      .users('NUaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
      .segmentMemberships('segment')
      .remove()
      .then(segment_membership => console.log(segment_membership.accountSid))
      .done();
