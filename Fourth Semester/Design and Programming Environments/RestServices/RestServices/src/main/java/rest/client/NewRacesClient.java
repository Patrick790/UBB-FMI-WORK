package rest.client;

import com.example.Race;
import com.services.rest.ServiceException;
import org.springframework.http.HttpRequest;
import org.springframework.http.client.ClientHttpRequestExecution;
import org.springframework.http.client.ClientHttpRequestInterceptor;
import org.springframework.http.client.ClientHttpResponse;
import org.springframework.web.client.HttpClientErrorException;
import org.springframework.web.client.ResourceAccessException;
import org.springframework.web.client.RestClient;

import java.io.IOException;
import java.util.concurrent.Callable;

import static org.springframework.http.MediaType.APPLICATION_JSON;

public class NewRacesClient {
    private final RestClient restClient = RestClient.builder()
            .requestInterceptor(new CustomRestClientInterceptor())
            .build();

    public static final String URL = "http://localhost:8080/temarest/races";

    public Race[] getAll() {
        return execute(() -> restClient.get().uri(URL).retrieve().body(Race[].class));
    }

    public Race getById(Long id) {
        return execute(() -> restClient.get().uri(String.format("%s/%s", URL, id)).retrieve().body(Race.class));
    }

    public Race create(Race race) {
        return execute(() -> restClient.post().uri(URL).contentType(APPLICATION_JSON).body(race).retrieve().body(Race.class));
    }



    public Race update(Long id, Race race) {
        return execute(() -> restClient.put().uri(String.format("%s/%s", URL, id)).contentType(APPLICATION_JSON).body(race).retrieve().body(Race.class));
    }

    public void delete(Long id) {
        execute(() -> restClient.delete().uri(String.format("%s/%s", URL, id)).retrieve().toBodilessEntity());
    }

    private <T> T execute(Callable<T> callable) {
        try {
            return callable.call();
        } catch (ResourceAccessException | HttpClientErrorException e) { // server down, resource exception
            throw new ServiceException(e);
        } catch (Exception e) {
            throw new ServiceException(e);
        }
    }

    public class CustomRestClientInterceptor implements ClientHttpRequestInterceptor {

        @Override
        public ClientHttpResponse intercept(HttpRequest request, byte[] body, ClientHttpRequestExecution execution) throws IOException {
            System.out.println("Sending a " + request.getMethod() + " request to " + request.getURI() + " and body [" + new String(body) + "]");
            ClientHttpResponse response = null;
            try {
                response = execution.execute(request, body);
                System.out.println("Got response code " + response.getStatusCode());
            } catch (IOException ex) {
                System.err.println("Eroare executie " + ex);
            }
            return response;
        }
    }
}
