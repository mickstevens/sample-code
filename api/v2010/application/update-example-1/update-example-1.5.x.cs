// Install the C# / .NET helper library from twilio.com/docs/csharp/install

using System;
using Twilio;
using Twilio.Converters;
using Twilio.Rest.Api.V2010.Account;


class Program 
{
    static void Main(string[] args)
    {
        // Find your Account Sid and Token at twilio.com/console
        const string accountSid = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
        const string authToken = "your_auth_token";

        TwilioClient.Init(accountSid, authToken);

        var application = ApplicationResource.Update(
            pathSid: "AP2a0747eba6abf96b7e3c3ff0b4530f6e",
            smsUrl: new Uri("http://demo.twilio.com/docs/sms.xml"),
            voiceUrl: new Uri("http://demo.twilio.com/docs/voice.xml")
        );

        Console.WriteLine(application.AccountSid);
    }
}
