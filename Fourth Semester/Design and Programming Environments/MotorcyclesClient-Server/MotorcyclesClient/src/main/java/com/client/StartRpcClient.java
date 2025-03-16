package com.client;


import java.io.IOException;
import java.util.Properties;

public class StartRpcClient {

    private static final int defaultPort = 55555;

    private static final String defaultServer = "localhost";

    public static void main(String[] args) {
        Properties clientProps = new Properties();
        try {
            clientProps.load(StartRpcClient.class.getResourceAsStream("/motorcyclesclient.properties"));
            System.out.println("Client properties set. ");
            clientProps.list(System.out);
        } catch (IOException e) {
            System.err.println("Cannot find motorcyclesclient.properties " + e);
            return;
        }

        String serverIP = clientProps.getProperty("motorcycles.server.host", defaultServer);
        int serverPort = defaultPort;

        try{
            serverPort=Integer.parseInt(clientProps.getProperty("chat.server.port"));
        }catch(NumberFormatException ex){
            System.err.println("Wrong port number "+ex.getMessage());
            System.out.println("Using default port: "+defaultPort);
        }
        System.out.println("Using server IP "+serverIP);
        System.out.println("Using server port "+serverPort);


    }
}
