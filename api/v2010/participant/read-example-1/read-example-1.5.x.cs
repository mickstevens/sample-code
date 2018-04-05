// Install the C# / .NET helper library from twilio.com/docs/csharp/install

using System;
using Twilio;
using Twilio.Rest.Api.V2010.Account.Conference;


class Program 
{
    static void Main(string[] args)
    {
        // Find your Account Sid and Token at twilio.com/console
        const string accountSid = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
        const string authToken = "your_auth_token";

        TwilioClient.Init(accountSid, authToken);

        var participants = ParticipantResource.Read(
            pathConferenceSid: "CFbbe4632a3c49700934481addd5ce1659"
        );

        foreach(var record in participants) {
           Console.WriteLine(record.AccountSid);
        }
    }
}
