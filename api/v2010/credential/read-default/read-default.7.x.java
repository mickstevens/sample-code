// Install the Java helper library from twilio.com/docs/java/install

import com.twilio.Twilio;
import com.twilio.base.ResourceSet;
import com.twilio.rest.api.v2010.account.sip.credentiallist.Credential;

public class Example {
    // Find your Account Sid and Token at twilio.com/console
    public static final String ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    public static final String AUTH_TOKEN = "your_auth_token";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
        ResourceSet<Credential> credentials = 
            Credential.reader("CLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa")
            .read();

        for(Credential record : credentials) {
            System.out.println(record.getSid());
        }
    }
}