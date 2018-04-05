// Install the Java helper library from twilio.com/docs/java/install

import com.twilio.Twilio;
import com.twilio.converter.Promoter;
import com.twilio.rest.chat.v2.service.Role;

public class Example {
    // Find your Account Sid and Token at twilio.com/console
    public static final String ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    public static final String AUTH_TOKEN = "your_auth_token";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
        Role role = Role.updater(
                "ISaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "RLaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                Promoter.listOfOne("permission"))
            .update();

        System.out.println(role.getSid());
    }
}