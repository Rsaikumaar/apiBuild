import com.mongodb.MongoClient;
import com.mongodb.MongoClientURI;
import com.mongodb.client.MongoDatabase;

public class mongo {
    public static void main(String[] args) {
        // MongoDB connection URI
        String connectionString = "mongodb://username:password@hostname:port/database";

        // Create a MongoClient
        MongoClientURI uri = new MongoClientURI(connectionString);
        MongoClient mongoClient = new MongoClient(uri);

        // Get the database
        MongoDatabase database = mongoClient.getDatabase("your_database_name");

        // Perform operations on the database
        // Example: database.getCollection("your_collection_name").find()...

        // Close the connection
        mongoClient.close();
    }
}
