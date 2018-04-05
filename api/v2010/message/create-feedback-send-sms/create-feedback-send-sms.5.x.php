<?php

// Update the path below to your autoload.php,
// see https://getcomposer.org/doc/01-basic-usage.md
require_once '/path/to/vendor/autoload.php';

use Twilio\Rest\Client;

// Your Account Sid and Auth Token from twilio.com/console
$sid    = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
$token  = "your_auth_token";
$twilio = new Client($sid, $token);

$message = $twilio->messages
                  ->create("+15558675310",
                           array(
                               'body' => "Open to confirm: http://yourserver.com/confirm?id=1234567890",
                               'from' => "+15017122661",
                               'provideFeedback' => False
                           )
                  );

print($message.sid);