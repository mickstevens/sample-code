// Install the Java helper library from twilio.com/docs/java/install

import com.twilio.Twilio;
import com.twilio.base.ResourceSet;
import com.twilio.rest.messaging.v1.service.AlphaSender;

public class Example {
    // Find your Account Sid and Token at twilio.com/console
    public static final String ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    public static final String AUTH_TOKEN = "your_auth_token";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
        ResourceSet<AlphaSender> alphaSenders = 
            AlphaSender.reader("MG2172dd2db502e20dd981ef0d67850e1a")
            .read();

        for(AlphaSender record : alphaSenders) {
            System.out.println(record.getSid());
        }
    }
}