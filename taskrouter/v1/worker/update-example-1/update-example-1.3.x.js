// Download the helper library from https://www.twilio.com/docs/node/install
// Your Account Sid and Auth Token from twilio.com/console
const accountSid = 'ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX';
const authToken = 'your_auth_token';
const client = require('twilio')(accountSid, authToken);

client.taskrouter.workspaces('WSXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                 .workers('WKXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX')
                 .update({attributes: `{"type":"support"}`})
                 .then(worker => console.log(worker.accountSid))
                 .done();
