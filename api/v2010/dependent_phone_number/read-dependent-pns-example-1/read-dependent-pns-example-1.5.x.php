<?php

// Update the path below to your autoload.php,
// see https://getcomposer.org/doc/01-basic-usage.md
require_once '/path/to/vendor/autoload.php';

use Twilio\Rest\Client;

// Your Account Sid and Auth Token from twilio.com/console
$sid    = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
$token  = "your_auth_token";
$twilio = new Client($sid, $token);

$dependentPhoneNumbers = $twilio->addresses("AD2a0747eba6abf96b7e3c3ff0b4530f6e")
                                ->dependentPhoneNumbers
                                ->read();

foreach ($dependentPhoneNumbers as $record) {
    print($record->sid);
}