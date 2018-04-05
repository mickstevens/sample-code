// Install the C# / .NET helper library from twilio.com/docs/csharp/install

using System;
using Twilio;
using Twilio.Rest.Api.V2010.Account.Sip.CredentialList;


class Program 
{
    static void Main(string[] args)
    {
        // Find your Account Sid and Token at twilio.com/console
        const string accountSid = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
        const string authToken = "your_auth_token";

        TwilioClient.Init(accountSid, authToken);

        var credential = CredentialResource.Create(
            pathCredentialListSid: "CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
            username: "Username",
            password: "Password"
        );

        Console.WriteLine(credential.Sid);
    }
}
