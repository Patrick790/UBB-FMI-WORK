package start;

import com.example.Race;
import com.services.rest.ServiceException;
import org.springframework.web.client.RestClientException;
import rest.client.NewRacesClient;

public class StartRestClientClient {
    private final static NewRacesClient racesClient = new NewRacesClient();

    public static void main(String[] args) {
        Race raceT = new Race(1200);
        try {
            System.out.println("Adding a new race " + raceT);
            show(() -> {
                Race createdRace = racesClient.create(raceT);
                raceT.setId(createdRace.getId());
                System.out.println(createdRace);
            });

            System.out.println("\nPrinting all races ...");
            show(() -> {
                Race[] res = racesClient.getAll();
                for (Race r : res) {
                    System.out.println(r.getId() + ": " + r.getCapacity());
                }
            });

            System.out.println("\nUpdating race with id=" + raceT.getId());
            raceT.setCapacity(1300);
            show(() -> System.out.println(racesClient.update(raceT.getId(), raceT)));

            System.out.println("\nInfo after update:");
            show(() -> System.out.println(racesClient.getById(raceT.getId())));

        } catch (RestClientException ex) {
            System.out.println("Exception ... " + ex.getMessage());
        }

        System.out.println("\nInfo for race with id=38");
        show(() -> System.out.println(racesClient.getById(38L)));

        System.out.println("\nDeleting race with id=" + raceT.getId());
        show(() -> racesClient.delete(raceT.getId()));
    }

    private static void show(Runnable task) {
        try {
            task.run();
        } catch (ServiceException e) {
            System.out.println("Service exception" + e);
        }
    }
}
