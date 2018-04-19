// Install the Java helper library from twilio.com/docs/java/install

import com.twilio.Twilio;
import com.twilio.rest.api.v2010.account.OutgoingCallerId;

public class Example {
    // Find your Account Sid and Token at twilio.com/console
    public static final String ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
    public static final String AUTH_TOKEN = "your_auth_token";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
        OutgoingCallerId outgoingCallerId = OutgoingCallerId.updater(
                "PNe536d32a3c49700934481addd5ce1659")
            .setFriendlyName("My Second Line").update();

        System.out.println(outgoingCallerId.getSid());
    }
}