// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
const accountSid = 'ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

client.preview.sync.services('ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                   .syncMaps('MPaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
                   .syncMapItems('key')
                   .remove()
                   .then(sync_map_item => console.log(sync_map_item.key))
                   .done();
