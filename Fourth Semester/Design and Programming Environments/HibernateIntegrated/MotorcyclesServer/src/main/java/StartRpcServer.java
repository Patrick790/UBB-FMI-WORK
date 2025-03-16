import com.example.*;
import com.hibernate.user.UserHibernateRepository;
import com.hibernate.user.User;
import com.hibernate.user.UserRepository;
import com.network.utils.AbstractServer;
import com.network.utils.MotorcyclesRpcConcurrentServer;
import com.server.MotorcyclesServicesImpl;
import com.services.IMotorcyclesServices;

import java.io.IOException;
import java.rmi.ServerException;
import java.util.Properties;

public class StartRpcServer {

    private static final int defaultPort = 55555;

    public static void main(String[] args) {
        Properties serverProps = new Properties();
        try {
            serverProps.load(StartRpcServer.class.getResourceAsStream("/motorcyclesServer.properties"));
            System.out.println("Server properties set. ");
            serverProps.list(System.out);
        } catch (IOException e) {
            System.err.println("Cannot find motorcyclesServer.properties " + e);
            return;
        }

        UserRepository userRepo = new UserHibernateRepository();
        IParticipantRepository participantRepo = new ParticipantDBRepository(serverProps);
        IRaceRepository raceRepo = new RaceDBRepository(serverProps);
        IRegistrationRepository registrationRepo = new RegistrationDBRepository(serverProps);
        IMotorcyclesServices motorcyclesServerImpl = new MotorcyclesServicesImpl(userRepo, participantRepo, raceRepo, registrationRepo);
        int motorcyclesServerPort = defaultPort;
        try {
            motorcyclesServerPort = Integer.parseInt(serverProps.getProperty("com.server.port"));
        } catch (NumberFormatException nef) {
            System.err.println("Wrong  Port Number" + nef.getMessage());
            System.err.println("Using default port " + defaultPort);
        }

        System.out.println("Starting server on port: " + motorcyclesServerPort);
        AbstractServer server = new MotorcyclesRpcConcurrentServer(motorcyclesServerPort, motorcyclesServerImpl);
        try {
            server.start();
        } catch (ServerException e) {
            System.err.println("Error starting the server" + e.getMessage());
        } finally {
            try {
                server.stop();
            } catch (ServerException e) {
                System.err.println("Error stopping server " + e.getMessage());
            }
        }

    }
}
