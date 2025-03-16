import com.network.RpcConcurrentServer;
import com.network.utils.AbstractServer;
import com.persistence.games.GameRepository;
import com.persistence.games.IGameRepository;
import com.persistence.players.IPlayerRepository;
import com.persistence.players.PlayerRepository;
import com.server.ServiceImplementations;
import com.services.IService;

import java.io.IOException;
import java.util.Properties;

public class StartServer {
    private final static int defaultPort = 55555;

    public static void main(String[] args) throws Exception {
        Properties serverProperties = new Properties();
        try {
            serverProperties.load(StartServer.class.getResourceAsStream("/bd.config"));
            System.out.println("Server properties set. ");
            serverProperties.list(System.out);
        } catch (IOException e) {
            System.err.println("Cannot find properties " + e);
            return;
        }

        IPlayerRepository playerRepository = new PlayerRepository(serverProperties);

        IGameRepository gameRepository = new GameRepository();


        IService service = new ServiceImplementations(playerRepository, gameRepository);
        var b=service.getScores();
        for(var i:b){
            System.out.println(i);
        }

        int serverPort = defaultPort;
        try {
            serverPort = Integer.parseInt(serverProperties.getProperty("server.port"));
        } catch (NumberFormatException nef) {
            System.err.println("Wrong  Port Number" + nef.getMessage());
            System.err.println("Using default port " + defaultPort);
        }

        AbstractServer server = new RpcConcurrentServer(serverPort, service);
        try {
            server.start();
        } catch (Exception e) {
            System.err.println("Error starting the server" + e.getMessage());
        } finally {
            try {
                server.stop();
            } catch (Exception e) {
                System.err.println("Error stopping server " + e.getMessage());
            }
        }
    }
}
