package start;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;

import java.util.Properties;

@ComponentScan({"com.example", "com.services.rest"})
@SpringBootApplication
public class StartRestServices {
    public static void main(String[] args) {

        SpringApplication.run(StartRestServices.class, args);
    }

    @Bean(name="props")
    public Properties getBdProperties(){
        Properties props = new Properties();
        props.setProperty("motorcycles.jdbc.driver", "org.sqlite.JDBC");
        props.setProperty("motorcycles.jdbc.url", "jdbc:sqlite:C:/Users/ardel/IdeaProjects/databases/motorcycles");
        return props;
    }
}