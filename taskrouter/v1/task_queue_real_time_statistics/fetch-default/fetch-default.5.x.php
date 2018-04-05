<?php

// Update the path below to your autoload.php,
// see https://getcomposer.org/doc/01-basic-usage.md
require_once '/path/to/vendor/autoload.php';

use Twilio\Rest\Client;

// Your Account Sid and Auth Token from twilio.com/console
$sid    = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
$token  = "your_auth_token";
$twilio = new Client($sid, $token);

$task_queue_real_time_statistics = $twilio->taskrouter->v1->workspaces("WSaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                                                          ->taskQueues("WQaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
                                                          ->realTimeStatistics()
                                                          ->fetch();

print($task_queue_real_time_statistics.accountSid);