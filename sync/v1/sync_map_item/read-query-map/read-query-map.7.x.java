// Install the Java helper library from twilio.com/docs/java/install

import com.twilio.Twilio;
import com.twilio.base.ResourceSet;
import com.twilio.rest.sync.v1.service.syncmap.SyncMapItem;

public class Example {
    // Find your Account Sid and Token at twilio.com/console
    public static final String ACCOUNT_SID = "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa";
    public static final String AUTH_TOKEN = "your_auth_token";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
        ResourceSet<SyncMapItem> syncMapItems = SyncMapItem.reader(
                "ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX",
                "Players")
            .setFrom("steph_curry")
            .setOrder(SyncMapItem.QueryResultOrder.ASC)
            .read();

        for(SyncMapItem record : syncMapItems) {
            System.out.println(record.getKey());
        }
    }
}