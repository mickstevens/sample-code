// Install the C# / .NET helper library from twilio.com/docs/csharp/install

using System;
using System.Collections.Generic;
using Twilio;
using Twilio.Rest.Preview.Understand.Assistant.Intent;


class Program 
{
    static void Main(string[] args)
    {
        // Find your Account Sid and Token at twilio.com/console
        const string accountSid = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
        const string authToken = "your_auth_token";

        TwilioClient.Init(accountSid, authToken);

        var actions = new Dictionary<string, Object>()
        {
            {"say", "I was going to look for my missing watch, but I could never find the time."}
        };

        var intentActions = IntentActionsResource.Update(
            actions: actions,
            pathAssistantSid: "UAXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
            pathIntentSid: "tell-a-joke"
        );

        Console.WriteLine(intentActions.AssistantSid);
    }
}
