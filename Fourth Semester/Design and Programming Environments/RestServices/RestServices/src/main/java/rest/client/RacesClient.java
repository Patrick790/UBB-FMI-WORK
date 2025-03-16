package rest.client;

import com.example.Race;
import com.services.rest.ServiceException;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.ResourceAccessException;
import org.springframework.web.client.RestTemplate;

import java.util.concurrent.Callable;

public class RacesClient {
    public static final String URL = "http://localhost:8080/temarest/races";

    private final RestTemplate restTemplate = new RestTemplate();

    private <T> T execute(Callable<T> callable) {
        try {
            return callable.call();
        } catch (ResourceAccessException | HttpClientErrorException e) {
            throw new ServiceException(e);
        } catch (Exception e) {
            throw new ServiceException(e);
        }
    }

    public Race[] getAll() {
        return execute(() -> restTemplate.getForObject(URL, Race[].class));
    }

    public Race getById(Long id) {
        return execute(() -> restTemplate.getForObject(String.format("%s/%s", URL, id), Race.class));
    }

    public Race create(Race race) {
        return execute(() -> restTemplate.postForObject(URL, race, Race.class));
    }

    public void update(Race race) {
        execute(() -> {
            restTemplate.put(String.format("%s/%s", URL, race.getId()), race);
            return null;
        });
    }

    public void delete(Long id) {
        execute(() -> {
            restTemplate.delete(String.format("%s/%s", URL, id));
            return null;
        });
    }
}