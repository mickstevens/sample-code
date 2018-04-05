// Install the C# / .NET helper library from twilio.com/docs/csharp/install

using System;
using Twilio;
using Twilio.Rest.Chat.V1.Service;


class Program 
{
    static void Main(string[] args)
    {
        // Find your Account Sid and Token at twilio.com/console
        const string accountSid = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
        const string authToken = "your_auth_token";

        TwilioClient.Init(accountSid, authToken);

        var role = RoleResource.Delete(
            pathServiceSid: "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            pathSid: "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
        );
    }
}
